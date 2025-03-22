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
            cudaPackages.cuda_cudart
            cudaPackages.cuda_nvcc
            cudaPackages.cuda_cupti
            cudaPackages.libcublas
            cudaPackages.cuda_nvrtc
            cudaPackages.libcufft
            cudaPackages.libcurand
            cudaPackages.libcusolver
            cudaPackages.libcusparse
            cudaPackages.nccl
            cudaPackages.libnvjitlink
            #
            #
            #
            #

	          conda
            # Instala python 3.11
            python311
            (python311.withPackages (ps: with ps; [
              # Instala paquetes de python.
              # En teoría se puede usar pip install, pero lo ideal es usar sólo el flake
              pandas numpy matplotlib seaborn scikit-learn openpyxl
              xlrd jupyterlab yfinance pytz tensorflow keras
            ]))
          ];
        shellHook = ''
          echo "Entorno de desarrollo activado para IPSA Prediction :D"


          export PATH=${pkgs.cudatoolkit}/bin:$PATH
          export CUDA_HOME=${pkgs.cudatoolkit}
          export LD_LIBRARY_PATH=${pkgs.cudatoolkit}/lib:$LD_LIBRARY_PATH
          export LD_LIBRARY_PATH=${pkgs.cudaPackages.cudnn}/lib:$LD_LIBRARY_PATH
          export TF_CUDA_COMPUTE_CAPABILITIES="8.6" # Ajusta según tu GPU

        '';

        
        };
      });

}
