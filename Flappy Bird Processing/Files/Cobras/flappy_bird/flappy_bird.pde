PImage fond, sol, tubeHaut, tubeBas, oiseau, gameOver, startMsg; //Déclaration de toutes les variables images
PImage[] perso; //Déclaration d'un tableau d'image utilisé pour animer l'oiseau
int positionSol, tubeX, tubeY, hauteur, i= 0; //Déclaration des variable devant contenir des nombres entier
float  vitesse = 0.0; //Déclaration de la variable vitesse qui contient un nombre à virgule pour plus de précision
boolean finDuJeu = false; //Déclaration d'une variable pour savoir si le joueur à perdu ou non
boolean firstTime = true; //Déclaration d'une variable pour savoir si c'est la première partie du joueur ou non

void setup() // fonction appelé une unique fois au début du programme. Elle est utilisé pour initialiser les variables déclaré plus haut avec différentes valeurs
{
  size(288,512); //détermine la taille de la fenêtre de jeu
  fond = loadImage("background-day.png"); //On affecte à chaque variable PImage une des images présente dans le dossier "data" 
  sol = loadImage("base.png");
  tubeHaut = loadImage("tubeHaut.png");
  tubeBas = loadImage("tubeBas.png");
  oiseau = loadImage("yellowbird-upflap.png");
  gameOver = loadImage("gameover.png");
  startMsg = loadImage("message.png");
  perso = new PImage[3]; //On indique que le tableau pour animer l'oiseau disposera de 3 images
  perso[0] = loadImage("yellowbird-downflap.png"); //On attribut les différentes images pour animer l'oiseau dans le tableau, case par case
  perso[1] = loadImage("yellowbird-midflap.png");
  perso[2] = loadImage("yellowbird-upflap.png");
  tubeX = 300; // La position en X initiale des tuyaux
  tubeY = int(random(200, 300)); // La hauteur initiale des tuyaux
  vitesse = -5; // La vitesse initiale de l'oiseau
  hauteur = 100; // La hauteur initiale de l'oiseau
  finDuJeu = false; //Le joueur n'a pas encore perdu
}

void draw() // fonction principale qui va se relancer indéfiniment tant que le joueur ne quitte pas le jeux 
{
  //ci-dessous vous appellez toutes les fonctions du jeu dans l'ordre nécessaire.
 
  if (finDuJeu == false && firstTime == false) {
    changement();
    display();
    oiseau();
    jump();
    finDuJeu = chocOiseau();
  }
  else if (firstTime == true) {
    startGame();
  }
  else {
    GameOver();
  }
}

void GameOver()
{
  display();
  image(gameOver, 45, 192);
  if (keyPressed == true && key == 'r') {
    setup();
  }
}

void startGame()
{
  display();
  image(startMsg, 50, 100);
  if (keyPressed == true && key == ' ') {
    firstTime = false;
  }
  
}


boolean chocOiseau()
{
  if (100 + 30 >= tubeX && 100 <= tubeX + 50) {
    if (hauteur <= tubeY - 130 || hauteur + 24 >= tubeY)
      return (true);
  }
  if (hauteur >= 372) {
     return (true);
  } else {
     return (false);
  }
}


void jump()
{
  if (keyPressed == true && key == ' ') {
    vitesse = -4.5;
  }
}

void changement()
{
  positionSol -= 2;
  if (positionSol < -23)
    positionSol = 0;
  tubeX = tubeX - 2;
  if (tubeX < -52) {
    tubeX = 288;
    tubeY = int(random(200, 300));
  }
}

void oiseau()
{
  hauteur = int(hauteur + vitesse);
  vitesse = vitesse + 0.2;
  if (vitesse <= -0.5) {
    oiseau = perso[1];
  } else if (vitesse <= 0.5) {
    oiseau = perso[2];
  }
  else {
   oiseau = perso[0];
  }
}

void display() {
  clear();
  background(fond);
  image(tubeBas, tubeX, tubeY);
  image(tubeHaut, tubeX, tubeY - 450);
  image(sol, positionSol, 400);
  image(oiseau, 100, hauteur);
}
