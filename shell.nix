{ pkgs ? import <nixpkgs> {} }:

let
  unstable = import (fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz";
    sha256 = "sha256:0dcslr2lwfaclfl4pmbwb3yw27bnvwlqiif394d3d66vyd163dvy";
  }) {
    inherit (pkgs) system;
    config = pkgs.config;
  };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    unstable.deno
    gnumake
    nodejs_22
    python312
    python312Packages.pip
    uv
    unstable.supabase-cli
    tmux
  ];

  shellHook = ''
    echo "🚀 Starting development environment..."
  '';
}
