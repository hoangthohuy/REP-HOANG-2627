# nixpkgs-pin.nix — picks a specific snapshot of nixpkgs
let
  rev = "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a";     # the head of the nixos-26.05 branch
  sha256 = "1w9mxci1wr015v8cgmqibwwb6nx9lqpi51jimkl61fylhbn7snx9";  # safety checksum, see step 3
in
import (builtins.fetchTarball {
  url = "https://github.com/NixOS/nixpkgs/archive/${rev}.tar.gz";
  inherit sha256;
})