{ pkgs ? import <nixpkgs> {} }:

let
  unstable = import (fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz";
    sha256 = "sha256:1r4gklhwylxar9y2dxyikkzf3hl615dj1jzfy851p6kc33qm1ilm";
  }) {
    inherit (pkgs) system;
    config = pkgs.config;
  };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    unstable.deno
    nodejs_22
    python312
    python312Packages.pip
    uv
    unstable.supabase-cli
    tmux
  ];

  shellHook = ''
    echo "🚀 Starting development environment..."
    export COMPOSE_PROJECT_NAME="pydo"
  '';
}
