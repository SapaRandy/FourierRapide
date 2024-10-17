from visualisations.visualisation1 import run_tfd_analysis
from visualisations.visualisation2 import run_fft_analysis

def print_menu():
    print("\nChoisissez une option :")
    print("1. Exécuter l'analyse transformée de Fourier rapide")
    print("2. Exécuter l'analyse transformée de Fourier discrète")
    print("3. Exécuter les deux analyses")
    print("4. Quitter")

def get_user_choice():
    while True:
        try:
            choice = int(input("Entrez votre choix (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def main():
    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 1:
            print("Démarrage de l'analyse FFT...")
            run_fft_analysis()
            print("Analyse FFT terminée.")
        elif choice == 2:
            print("Démarrage de l'analyse TFD...")
            run_tfd_analysis()
            print("Analyse TFD terminée.")
        elif choice == 3:
            print("Démarrage de l'analyse FFT...")
            run_fft_analysis()
            print("Analyse FFT terminée.")
            print("\nDémarrage de l'analyse TFD...")
            run_tfd_analysis()
            print("Analyse TFD terminée.")
        elif choice == 4:
            print("Au revoir !")
            break

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()