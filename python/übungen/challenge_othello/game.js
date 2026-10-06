const $ = (id) => document.getElementById(id);

// Sprites
function setSprite(element, x, y, width, height, scale, yScale = scale) {
    element.style.width = `${width * scale}px`;
    element.style.height = `${height * yScale}px`;

    element.style.backgroundSize = `${500 * scale}px ${208 * yScale}px`;
    element.style.backgroundPosition = `${-x * scale}px ${-y * yScale}px`;

    return element;
}

function createSprite(x, y, width, height, scale) {
    const element = document.createElement('div');

    element.className = 'spr';

    return setSprite(
        element,
        x,
        y,
        width,
        height,
        scale
    );
}

// Chip animation
function getChipFrame(frame) {
    const frameIndex = frame < 8
        ? 7 - frame
        : frame - 8;

    const x = frame < 8 ? 186 : 209;
    const y = 13 + 23 * frameIndex;

    return [x, y, 23, 24];
}

function createChipSprite(frame, scale) {
    return createSprite(
        ...getChipFrame(frame),
        scale
    );
}


// Sound
const SOUNDS = {
    music: '',
    letter: '',
    spin: '',
    build: '',
    whoosh: ''
};

const SFX_VOLUME = 0.6;
const MUSIC_VOLUME = 0.5;

let backgroundMusic;
let musicStarted = false;

function playSound(name) {
    const sound = SOUNDS[name];

    if (!sound) {
        return;
    }

    const audio = new Audio(sound);

    audio.volume = SFX_VOLUME;

    // Ignore autoplay errors.
    audio.play().catch(() => {});
}

function fadeInAudio(audio, targetVolume, duration) {
    const startTime = performance.now();

    const fadeTimer = setInterval(() => {
        const elapsed = performance.now() - startTime;
        const progress = Math.min(1, elapsed / duration);

        audio.volume = targetVolume * progress;

        if (progress === 1) {
            clearInterval(fadeTimer);
        }
    }, 50);
}

function startMusic() {
    if (musicStarted || !SOUNDS.music) {
        return;
    }

    if (!backgroundMusic) {
        backgroundMusic = new Audio(SOUNDS.music);
        backgroundMusic.loop = true;
        backgroundMusic.volume = 0;
    }

    backgroundMusic
        .play()
        .then(() => {
            musicStarted = true;
            fadeInAudio(backgroundMusic, MUSIC_VOLUME, 4000);
        })
        .catch(() => {});
}

addEventListener('pointerdown', startMusic);



// Title screen
const TITLE_SCALE = Math.max(
    2,
    Math.min(6, Math.floor((innerWidth - 40) / 175))
);
const TITLE_SPRITES = [
    [3, 8, 19, 27],
    [29, 6, 10, 30],
    [50, 5, 20, 31],
    [81, 13, 18, 23],
    [105, 5, 9, 30],
    [105, 5, 9, 30],
    'chip',
    [122, 3, 17, 32]
];
const titleScreen = $('titlescreen');
titleScreen.style.gap = `${TITLE_SCALE * 2}px`;
titleScreen.style.setProperty('--fl', `${TITLE_SCALE * 2}px`);
const START_DELAY = 100;

let energy = 0;
let spinning = false;
let starting = false;
let ready = false;
let spinPosition = 0;
let spinTimer;

// Create the title sprites.
const titleElements = TITLE_SPRITES.map((sprite, index) => {
    let element;

    if (sprite === 'chip') {
        element = createChipSprite(0, TITLE_SCALE);
    } else {
        element = createSprite(
            ...sprite,
            TITLE_SCALE
        );
    }

    if (index === 6) {
        element.classList.add('title-spin');
    }

     element.classList.add('title');


    element.style.animationDelay = `${-index * 0.35}s`;

    titleScreen.append(element);

    return element;
});


// Play the title animation.
titleElements.forEach((element, index) => {
    setTimeout(() => {
        element.classList.add('on');

        playSound('letter');

        // The last letter finishing means the title is ready.
        if (index === 7) {
            setTimeout(() => {
                ready = true;
                $('hint').classList.add('on');
            }, 400);
        }
    }, 1000 + index * 260);
});


// Spin animation
const SPIN_LENGTH = 31
function getSpinFrame(position) {
    if (position < 15) {
        return { frame: position, flipped: false };
    }

    return { frame: 30 - position, flipped: true };
}

function spinStep() {
    clearTimeout(spinTimer);
    spinPosition = (spinPosition + 1) % SPIN_LENGTH;

    const { frame, flipped } = getSpinFrame(spinPosition);

    setSprite(
        titleElements[6],
        ...getChipFrame(frame),
        TITLE_SCALE
    );
    titleElements[6].style.scale = flipped ? '-1 1' : '1 1';

    if (energy <= 0 && (frame === 0 || frame === 15)) {
        spinning = false;
        return;
    }

    const delay = Math.max(1, 100 - energy * 30);
    spinTimer = setTimeout(spinStep, delay);
}


// Slowly drain energy while the player isn't starting the game.
setInterval(() => {
    if (!starting) {
        energy = Math.max(0,energy - 0.25);
    }
}, 300);



// Spin button
document.querySelector('.title-spin').onclick  = () => {
    if (starting || !ready) {
        return;
    }

    startMusic();

    energy += 1;

    playSound('spin');

    spinning = true;
    spinStep();

    // Enough energy means the game can start.
    if (energy >= 4) {
        starting = true;

        playSound('build');

        setTimeout(
            goToGame,
            START_DELAY
        );
    }
};

// Transition to game

function goToGame() {
    const wipe = $('wipe');

    $('start').classList.add('out');
    wipe.classList.add('in');

    playSound('whoosh');

    setTimeout(() => {
        const startScreen = $('start');
        const game = $('game');

        startScreen.hidden = true;
        startScreen.classList.remove('out');

        game.hidden = false;

        wipe.classList.remove('in');
        wipe.classList.add('out');

        setTimeout(() => {
            // Reset the transition so it can be used again.
            wipe.style.transition = 'none';
            wipe.classList.remove('out');

            // Force the browser to apply the reset.
            void wipe.offsetWidth;
            wipe.style.transition = '';

            energy = 0;
            starting = false;
        }, 800);
    }, 800);
}