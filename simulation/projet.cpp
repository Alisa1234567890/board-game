#include <iostream>
#include <math.h>
#include <Grapic.h>
using namespace std;
using namespace grapic;

const int MAX=100;
const int DIMW=1000;
const int longeur=50;
const float VMAX=10;
const int C=1;

int elements() {
    int n;
    n=(DIMW/longeur)+1;
    return n;
}

struct couleur {
    unsigned char r, g, b;
};

struct casee {
    int etat;
    couleur c;
    float vitesse;
    int temps;
    float fp_vx_plus, fp_vx_moins, fp_vy_plus, fp_vy_moins;
    int xCaseRouge, yCaseRouge;
    bool noir;
};


struct grille {
    casee tab[MAX][MAX];
    int nb_cases;
    int dx, dy;
    bool stop_propagation;
    int nb_rouges;
    int nb_iter;
    float p1, p2;
    bool vr=false; //si on veut faire varier la valeur de vraisemblance
};

struct  vraisemblance {
    int nb;
    float tab[MAX];
};

couleur interpolation (couleur c1, couleur c2, int i) {
    couleur c;
    c.r=(1-i)*c1.r+i*c2.r;
    c.g=(1-i)*c1.g+i*c2.g;
    c.b=(1-i)*c1.b+i*c2.b;
    return c;
}

void affiche_vraisemblance(vraisemblance v) {
    int i;
    for (i=0; i<v.nb; i++) {
        cout<<"p1: "<<v.tab[i]<<endl;
    }
}

void affiche_case(casee c) {
    if (c.etat==0) {
        cout<<"arbre vert"<<endl;
    } else if (c.etat==1) {
        cout<<"arbre en feu"<<endl;
    } else {
        cout<<"arbre brule"<<endl;
    }
    cout<<"vitesse: "<<c.vitesse<<endl;
    cout<<"temps: "<<c.temps<<endl;
    cout<<"facteur de propagation vx plus: "<<c.fp_vx_plus<<endl;
    cout<<"facteur de propagation vx moins: "<<c.fp_vx_moins<<endl;
    cout<<"facteur de propagation vy plus: "<<c.fp_vy_plus<<endl;
    cout<<"facteur de propagation vy moins: "<<c.fp_vy_moins<<endl;
    cout<<"abscisse: "<<c.xCaseRouge<<endl;
    cout<<"ordonnee: "<<c.yCaseRouge<<endl;
}

void affiche_grille(grille g) {
    cout<<"Nombre de cases: "<<g.nb_cases<<endl;
    cout<<"Largeur: "<<g.dx<<endl;
    cout<<"Longeur: "<<g.dy<<endl;
    if (g.stop_propagation==true) {
        cout<<"Il y a une propagation"<<endl;
    } else {
        cout<<"Il n'y a pas de propagation"<<endl;
    }
    cout<<"Numero d'iteration: "<<g.nb_iter<<endl;
    cout<<"Vraisemblance p1: "<<g.p1<<endl;
    cout<<"Vraisemblance p2: "<<g.p2<<endl;
    int i, j;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            affiche_case(g.tab[i][j]);
        }
    }
    cout<<"fin de grille"<<endl;
}

void facteur_propagation(grille &g) {
    int i,j;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            if (g.tab[i][j].vitesse==0) {
                g.tab[i][j].fp_vx_plus=1;
                g.tab[i][j].fp_vx_moins=1;
                g.tab[i][j].fp_vy_plus=1;
                g.tab[i][j].fp_vy_moins=1;
            } else {
                g.tab[i][j].fp_vx_plus=(g.tab[i][j].vitesse/VMAX)*((1-g.p1)/g.p1)+1;
                g.tab[i][j].fp_vx_moins=1-(g.tab[i][j].vitesse/VMAX);
                g.tab[i][j].fp_vy_plus=1;
                g.tab[i][j].fp_vy_moins=1;
            }
        }
    }

}

bool cases_rouges(grille &g) {
    int i, j;
    bool cr=false;

    for (i=0; i<g.dy; i++) {
        for (j=0; j<g.dx; j++) {
            if (g.tab[i][j].etat==1) {
                cr=true;

            }
        }
    }
    return cr;
}


int nb_r(grille g) {
    int r;
    r=0;
    int i,j;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            if (g.tab[i][j].etat==1) {
                r++;
            }
        }
    }
    return r;
}

int nb_n(grille g) {
    int n;
    n=0;
    int i,j;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            if (g.tab[i][j].etat==2) {
                n++;
            }
        }
    }
    return n;
}

int nb_v(grille g) {
    int v;
    v=0;
    int i,j;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            if (g.tab[i][j].etat==0) {
                v++;
            }
        }
    }
    return v;
}

void drawScore(grille g)
{
    int r=nb_r(g);
    int n=nb_n(g);
    int v=nb_v(g);
    color(255, 255, 255);
    fontSize(30);
    print(DIMW/2+70, DIMW - 40,"nombre des arbres en feu:");
    print(DIMW -70, DIMW - 40,r);
    print(DIMW/2+70, DIMW - 80,"nombre des arbres brules:");
    print(DIMW -70, DIMW - 80,n);
    print(DIMW/2+70, DIMW - 120,"nombre des arbres verts:");
    print(DIMW -70, DIMW - 120,v);
}

void percentage(float &r, float &v, float &n, grille g) {
    int ri=nb_r(g)*100;
    r=ri/g.nb_cases;
    int ni=nb_n(g)*100;
    n=ni/g.nb_cases;
    int vi=nb_v(g)*100;
    v=vi/g.nb_cases;

}

void draw_p(grille &g) {
    float r, v, n;
    percentage(r,v,n,g);
    color(255, 255, 255);
    fontSize(30);
    print(1, 60,"pourcentage des arbres en feu: ~");
    print(460, 60,r);
    print(545, 60,"%");
    print(1, 30,"pourcentage des arbres brules: ~");
    print(460, 30,n);
    print(545, 30,"%");
    print(1, 1,"pourcentage des arbres verts: ~");
    print(450, 1,v);
    print(535, 1,"%");
    couleur c, c1, c2;
    c1= {0,0,255};
    c2= {200,0,50};
    c=interpolation(c1,c2,n);  //couleur de "vraisemblance p1" interpole entre deux couleurs en fonction de nombre de cases noirs
    color(c.r,c.g,c.b);
    fontSize(30);
    if (g.vr==false) {
        print(5,DIMW-55,"vraisemblance p1 = 0.5*C");
    } else {
        print(5,DIMW-55,"vraisemblance p1 varie");
    }
}

void draw(grille &g) {
    int i,j;
    float pasj=DIMW/g.dy;
    float pasi=DIMW/g.dx;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            switch(g.tab[i][j].etat) {
            case 0:
                color(0,250,0);
                break;
            case 1:
                color(250,0,0);
                break;
            case 2:
                color(50,0,50);
                break;
            default:
                color(0,0,0);
                break;
            }
            rectangleFill(j*pasj,i*pasi,(j+1)*pasj,(i+1)*pasi);
        }
    }

}



void init(grille &g, int nb, vraisemblance &v) {
    g.nb_cases=nb;
    g.dx=sqrt(g.nb_cases);
    g.dy=sqrt(g.nb_cases);
    int i,j;
    for (i=0; i<v.nb; i++) {
        v.tab[i]=0;
    }
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            g.tab[i][j].etat=0;
            g.tab[i][j].temps=0;
            g.tab[i][j].noir=false;
        }
    }
    int l;
    for (l=0; l<3; l++) {
        i=rand()%g.dx;
        j=rand()%g.dy;
        g.tab[i][j].etat=1;
    }
    g.nb_rouges=3;
    g.nb_iter=0;
    g.p1=0.5*C;
    g.p2=0.3;
    v.tab[0]=g.p1;
    v.nb=1;
    //g.decor=im;
}


void simulation(grille &g, vraisemblance &v,Plot &p) {
    srand(time(NULL));
    int x,y;
    int nbi;
    int i, j;
    mousePos(x,y);
    float pasj=DIMW/g.dy;  //pour dessiner les carres
    float pasi=DIMW/g.dx;
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            if(y>=i*pasi and y<(i+1)*pasi and x>=j*pasj and x<(j+1)*pasj and g.tab[i][j].etat==0) {  //si le souris est sur l'arbre particulier
                g.tab[i][j].etat=1;
            }
        }
    }

    int N;
    N=elements();
    bool casesrouges;
    float v_nb, r_nbn;
    int a,b;
    float nrb, nv;
    casesrouges=cases_rouges(g);
    if(casesrouges==true) {
        for (i=0; i<g.dx; i++) {
            for (j=0; j<g.dy; j++) {
                if (g.tab[i][j].etat==1) {
                    g.tab[i][j].xCaseRouge=j*pasj;
                    g.tab[i][j].yCaseRouge=i*pasi;
                    if (g.tab[i][j].xCaseRouge==DIMW) {   //cas d'arret
                        g.stop_propagation=true;
                    }
                    if (!g.stop_propagation) {
                        nv=rand()%100+1;   //valeur aleatoire
                        for (a=i-1; a<=i+1; a++) {   //parcourir des cases
                            for (b=j-1; b<=j+1; b++) {
                                if (a>=0 && a<DIMW && b>=0 && b<DIMW) {   //si l'extremite est atteint
                                    if (g.tab[a][b].noir==false) {
                                        if (nv<g.p1*100 and g.tab[a][b].etat!=1) {
                                            g.tab[a][b].etat=1; //propagation du feu
                                        }
                                    }
                                }
                            }
                        }
                    }
                    nrb=rand()%100+1;
                    if (nrb<g.p2*100) {
                        g.tab[i][j].etat=2;  //arbre brulee
                        g.tab[i][j].noir=true;

                    }
                }
            }
        }
        g.nb_iter++;
        v_nb=nb_v(g);
        r_nbn=nb_r(g)-g.nb_rouges;  //nouveaux cases rouges
        if (g.vr==true) {  //si la valeur de vraisemblance  p1 varie
            g.p1=(v_nb*r_nbn+(v_nb-r_nbn)*(1-g.p1))*g.p1;  //nouvelle valeur de vraisemblance
            if (g.p1<=0) {
                g.p1=0.5*C;
            }
        }
        g.nb_rouges=nb_r(g);  //nombre des cases rouges cette iteration
    } else {
        nbi=g.nb_iter;
        init(g,N*N,v);
        //plot_clear(p);
        g.nb_iter=g.nb_iter+nbi;  //nombre total des iteration
    }
    for (i=0; i<g.dx; i++) {
        for (j=0; j<g.dy; j++) {
            if (g.tab[i][j].etat==0) {
                g.tab[i][j].temps++;
            }
        }
    }

    v.tab[v.nb]=g.p1;  //ajouter vraisemblance p1 dans un tableau  structure de vraisemblance p1
    v.nb++;
}

const int MAXCH=10;

int main(int, char**) {
    winInit("grille",DIMW,DIMW+100);
    struct grille g;
    bool stop=false;
    vraisemblance v;
    Image img;
    img=image("data/image du foret.jpg");
    int N;
    char cha[MAXCH];
    char cha1[MAXCH];
    Plot p;
    plot_setSize(p,-1);
    N=elements();
    init(g,N*N,v);
    g.vr=false;
    bool simul=true;
    bool vraisemblance=false;  //vraisemblance ne varie pas
    int nbr, nbv, nbn;
    int temps;
    while (!stop) {
        winClear();
        temps=elapsedTime();
        if (temps<3) {  //les premiers 3 secondes a partir du demarrage du programme
            image_draw(img,0,0,DIMW-1,DIMW+99);
            //backgroundColor(0,250,0);
            color(255,255, 255);
            fontSize(35);
            print(DIMW/2-400, DIMW/2+100,"Simulation de la propagation d un feu de foret");
            fontSize(100);
            print(DIMW/2, DIMW/2,3-temps);  //temps avant la simulation commence
        } else {
            backgroundColor(250,250,250);
            draw(g);
            drawScore(g);
            draw_p(g);
            if (isKeyPressed(SDLK_DOWN)) {
                simul=false;  // pour demander si l'utilisateur souhaite afficher une grille
            }
            if (isKeyPressed(SDLK_UP)) {
                vraisemblance=true;  //pour demander si l'utilisateur souhaite afficher les valeurs de vraisemblance
            }
            if (isKeyPressed(SDLK_LEFT)) {
                g.vr=true;  //pour faire varier la valeur de vraisemblance p1
            }
            if (isKeyPressed(SDLK_RIGHT)) {
                g.vr=false;   //pour faire la valeur de vraisemblance constante
                g.p1=0.5*C;
            }
            if(simul==true) {
                simulation(g,v,p);
                nbr=nb_r(g);
                plot_add(p,g.nb_iter,nbr,0);  //nombre des cases rouges
                nbv=nb_v(g);
                plot_add(p,g.nb_iter,nbv,1);  //nombre des cases verts
                nbn=nb_n(g);
                plot_add(p,g.nb_iter,nbn,2);   //nombre des cases noirs
                color(50,50,50);
                plot_draw(p,10,DIMW,DIMW-10,DIMW+100);
            }
            if (simul==false) {   //pour demander si l'utilisateur souhaite afficher les valeurs de grille
                color(50,50,50);
                plot_draw(p,10,DIMW,DIMW-10,DIMW+100);
                cout<<"afficher grille?"<<endl;
                cin>>cha;
                if (strcmp(cha,"oui")==0) {
                    affiche_grille(g);
                    simul=true;
                } else {
                    simul=true;
                }
            }
            if (vraisemblance==true) {  //pour demander si l'utilisateur souhaite afficher les valeurs de vraisemblance
                cout<<"afficher les valeurs de vraisemblance?"<<endl;
                cin>>cha1;
                if (strcmp(cha1,"oui")==0) {
                    affiche_vraisemblance(v);
                    vraisemblance=false;
                } else {
                    vraisemblance=false;
                }
            }
        }
        stop=winDisplay();
        delay(500);
    }
    winQuit();
    return 0;
}# SImulation-de-la-propagation-d-un-feu-de-foret
