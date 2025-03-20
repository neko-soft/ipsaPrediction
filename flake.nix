{
  description = "Entorno de desarrollo modelo predicción IPSA";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };


  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system;
                                config.allowUnfree = true;
                              };
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [

            cudaPackages.cudatoolkit
            cudaPackages.cudnn

            # Instala python 3.11
            python311
            (python311.withPackages (ps: with ps; [
              # Instala paquetes de python.
              # En teoría se puede usar pip install, pero lo ideal es usar sólo el flake
              pandas numpy matplotlib seaborn scikit-learn openpyxl
              xlrd jupyterlab yfinance pytz torch torchvision 
              torchaudio
            ]))
          ];
        shellHook = ''
          echo "Entorno de desarrollo activado para IPSA Prediction :D"

          # Configuración de las variables de entorno CUDA
          export CUDA_PATH=${pkgs.cudatoolkit}
          export LD_LIBRARY_PATH=${pkgs.cudatoolkit}/lib:$LD_LIBRARY_PATH
          export PATH=${pkgs.cudatoolkit}/bin:$PATH

          # Asegurar que las variables de entorno de NVIDIA estén configuradas
          export WLR_NO_HARDWARE_CURSORS=1  # Hacer que Wayland no use los cursores de hardware de NVIDIA
          export __GLX_VENDOR_LIBRARY_NAME=nvidia
          export LIBVA_DRIVER_NAME=nvidia
        '';

        
        };
      });

}
