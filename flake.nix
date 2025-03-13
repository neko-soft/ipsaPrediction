{
  description = "Entorno de desarrollo modelo predicción IPSA";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Instala python 3.11
            python311
            (python311.withPackages (ps: with ps; [
              # Instala paquetes de python.
              # En teoría se puede usar pip install, pero lo ideal es usar sólo el flake
              pandas numpy matplotlib seaborn scikit-learn
            ]))
          ];
        shellHook = ''
          echo "Entorno de desarrollo activado para IPSA Prediction :D"
        '';
        };
      });
}
