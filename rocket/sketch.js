// CONSTANTES
const WIDTH = 900;
const HEIGHT = 900;
const BACKGROUND_COLOR = "black";

const STAR_COLOR = "white";
const STAR_NB = 15;
const STAR_SIZE_MIN = 2;
const STAR_SIZE_MAX = 12;
const STAR_SPEED = 1;

const ASTEROID_NB = 20;
const ASTEROID_SIZE_MIN = 30;
const ASTEROID_SIZE_MAX = 65;
const ASTEROID_SPEEDS = [4, 5, 7, 10];

const CAPSULE_SPEED = 10;
const CAPSULE_SIZE = 70;
const CAPSULE_Y = 150;

const GAME_OVER_WIDTH = 850;
const GAME_OVER_HEIGHT = 425;

const DIRECTION = {NONE: 0, LEFT: 1, RIGHT: 2};

const IMG_GAME_OVER = "ressources/game_over.png"
const IMG_CAPSULE = "ressources/capsule.png"
const IMG_ASTEROID_1 = "ressources/asteroid1.png"
const IMG_ASTEROID_2 = "ressources/asteroid2.png"
const IMG_ASTEROID_3 = "ressources/asteroid3.png"
const IMG_ASTEROID_4 = "ressources/asteroid4.png"

// VARIABLES
let game_over = false;
let stars = [];
let asteroids = [];
let capsule;
let game_over_img;

// CLASSES
// Définition de l'étoile
class Star {
    constructor() {
        this.position = createVector(0, 0);
        this.init();
    }

    init() {
        this.size = random(STAR_SIZE_MIN, STAR_SIZE_MAX);
        this.position.set(random(-this.size, WIDTH), random(-this.size, -HEIGHT));
        this.speed = STAR_SPEED * this.size;
    }

    display() {
        fill(STAR_COLOR);
        circle(this.position.x, this.position.y, this.size);
    }

    fall() {
        this.position.y += this.speed;
        if (this.position.y > HEIGHT)
            this.init();
    }
}

// Définition de l'astéroide
class Asteroid {
    constructor() {
        this.position = createVector(0, 0);
        this.init();
    }

    init() {
        this.size = random(ASTEROID_SIZE_MIN, ASTEROID_SIZE_MAX);
        this.position.set(random(-this.size, WIDTH), random(-this.size, -HEIGHT));
        this.speed = random(ASTEROID_SPEEDS);
        this.img = random(asteroids_img);
    }

    display() {
        image(
            this.img,
            this.position.x, this.position.y,
            this.size, this.size
            )
    }

    checkCollision(capsule) {
        if (this.position.y > HEIGHT)
            this.init();

        if (this.position.x < capsule.position.x + capsule.size &&
            this.position.x + this.size > capsule.position.x &&
            this.position.y < capsule.position.y + capsule.size &&
            this.position.y + this.size > capsule.position.y) {
            game_over = true;
        }
    }
    
    fall() {
        this.position.y += this.speed;
    }
}

// Définition de la capsule
class Capsule {
    constructor() {
        this.direction = "NONE"
        this.speed = CAPSULE_SPEED;
        this.size = CAPSULE_SIZE;
        this.position = createVector(WIDTH / 2 - this.size / 2,
            HEIGHT - CAPSULE_Y);
    }

    display() {
        image(capsule_img, this.position.x, this.position.y, this.size, this.size);
    }

    move() {
        if (this.direction === DIRECTION.LEFT && this.position.x > 0)
            this.position.x -= this.speed;
        if (this.direction === DIRECTION.RIGHT && this.position.x < HEIGHT - this.size)
            this.position.x += this.speed;
    }
}

// FONCTIONS
// Fonction executée avant setup pour charger des ressources
function preload() {
    game_over_img = loadImage(IMG_GAME_OVER)
    capsule_img = loadImage(IMG_CAPSULE)
    asteroids_img = [
        loadImage(IMG_ASTEROID_1),
        loadImage(IMG_ASTEROID_2),
        loadImage(IMG_ASTEROID_3),
        loadImage(IMG_ASTEROID_4)
    ]
}

// Fonction executée au lancement du jeu
function setup() {
    createCanvas(WIDTH, HEIGHT);
    
    capsule = new Capsule();

    for (var i = 0; i < STAR_NB; i++)
        stars.push(new Star());

    for (var i = 0; i < ASTEROID_NB; i++)
        asteroids.push(new Asteroid());
}

// Fonction executée en boucle tant que le jeu est ouvert
function draw() {
    if (!game_over) {
        clear();
        background(BACKGROUND_COLOR);

        for (const star of stars) {
            star.fall();
            star.display();
        }

        capsule.move();
        capsule.display();

        for (const asteroid of asteroids) {
            asteroid.fall();
            asteroid.checkCollision(capsule);
            asteroid.display();
        }
    } else
        image(game_over_img, WIDTH / 2 - GAME_OVER_WIDTH / 2,
            HEIGHT / 2 - GAME_OVER_HEIGHT / 2,
            GAME_OVER_WIDTH, GAME_OVER_HEIGHT)
}

// Fonction executée lorsqu'une touche est pressée
function keyPressed() {
    if (keyCode === LEFT_ARROW)
        capsule.direction = DIRECTION.LEFT;
    else if (keyCode === RIGHT_ARROW)
        capsule.direction = DIRECTION.RIGHT;
    else if (key === 'r' && game_over) {
        for (asteroid of asteroids)
            asteroid.init();
        game_over = false;
    }
}

// Fonction executée lorsqu'une touche est relachée
function keyReleased() {
    if (keyCode === LEFT_ARROW || keyCode === RIGHT_ARROW) {}
        capsule.direction = DIRECTION.NONE;
}
