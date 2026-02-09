# M-tronome-V5

## Mise en place prête à l’emploi (Windows autonome)

### 1) Générer l’EXE sur un poste de build
Prérequis : **Windows 10/11 64‑bit** + **Python 3.11+**.

Dans le dossier du projet, exécutez :
```powershell
.\build_windows.ps1
```

➡️ L’exécutable est généré ici :
```
.\dist\M-tronome-V5.exe
```

### 2) Déployer sur tous les postes
Copiez **uniquement** le fichier `M-tronome-V5.exe` sur chaque poste (par exemple `C:\M-tronome\`).

Créez un raccourci qui lance :
```
C:\M-tronome\M-tronome-V5.exe
```

### 3) Lancer l’application
- Double‑cliquez sur l’exe : l’app démarre sur le poste.
- Ouvrez ensuite : `http://localhost:8090`

### Variables optionnelles
- `METRONOME_HOST` (par défaut `0.0.0.0`)
- `METRONOME_PORT` (par défaut `8090`)
