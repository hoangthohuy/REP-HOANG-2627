let
  pkgs = import ./nixpkgs-pin.nix {};
  py = pkgs.python311;
in
pkgs.mkShell {
  packages = [ py pkgs.python311Packages.venvShellHook ];
  venvDir = ".venv";
  postVenvCreation = ''
    python -m pip install --upgrade pip
    if [ -f requirements.txt ]; then
      PIP_DISABLE_PIP_VERSION_CHECK=1 python -m pip install -r requirements.txt
    fi
  '';
}