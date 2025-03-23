# Predicción IPSA

La idea de este repo es crear un modelo que sea capaz de predecir el precio del [IPSA](https://www.spglobal.com/spdji/en/indices/equity/sp-ipsa/#overview), que es un índice bursátil de la bolsa de Santiago de Chile.

## Pendientes 
- [ ] Probar distintos métodos para el modelo de predicción.


## Como usar aceleración por GPU Nvidia con NixOS:


1) Hay que poner los substitutes en el config.nix

nix.settings = {
  substituters = [
    "https://nix-community.cachix.org"
	"https://cuda-maintainers.cachix.org"
  ];
  trusted-public-keys = [
    "nix-community.cachix.org-1:mB9FSh9qf2dCimDSUo8Zy7bkq5CX+/rkCWyvRCYg3Fs="
    "cuda-maintainers.cachix.org-1:0dq3bujKpuEPMCX6U4WylrUDZ9JyUG0VpVZa7CNfq5E="
  ];
};

Así está bien, no es necesario poner , entre cada entrada.

2) Después, en el flake tienes que usar "tensorflowWithCuda", o "TorchWithCuda", porque si instalas sólo "tensorflow" o "Torch", sólo va a instalar la versión para CPU.

3) Verificar cuál versión de python hay que usar, ya que no todos los tensorflow o torch de todas las versiones de python tienen los binarios, esto se hace con:

nix search nixpkgs tensorflowWithCuda
nix search nixpkgs torchWithCuda

El resultado debería ser algo tipo: 

$ nix search nixpkgs tensorflowWithCuda
* legacyPackages.x86_64-linux.python312Packages.tensorflowWithCuda (2.19.0)
  Computation using data flow graphs for scalable machine learning

* legacyPackages.x86_64-linux.python313Packages.tensorflowWithCuda (2.19.0)
  Computation using data flow graphs for scalable machine learning

$ nix search nixpkgs torchWithCuda
* legacyPackages.x86_64-linux.python312Packages.pytorchWithCuda (2.5.1)
  PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration

* legacyPackages.x86_64-linux.python312Packages.torchWithCuda (2.5.1)
  PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration

* legacyPackages.x86_64-linux.python313Packages.pytorchWithCuda (2.5.1)
  PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration

* legacyPackages.x86_64-linux.python313Packages.torchWithCuda (2.5.1)
  PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration

Ahí uno ve que para tensorflowWithCuda, sólo la versión de python 3.12 y 3.13 tienen binarios, lo mismo para torchWithCuda.

4) Finalmente, si las versiones de python con binarios no están en el nixpkgs estable, usar la versión unstable en el flake:

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

5) Configuración de NVIDIA en configuration.nix

Esto es lo mismo que sale por ahí en internet, así que es relativamente sensillo.:

hardware.graphics.enable = true;
services.xserver.videoDrivers = ["nvidia"];
hardware.nvidia = {
    modesetting.enable = true;
    powerManagement.enable = false;
    powerManagement.finegrained = false;
    open = false;
    nvidiaSettings = true;
    nvidiaPersistenced = true;
    package = config.boot.kernelPackages.nvidiaPackages.latest;
};