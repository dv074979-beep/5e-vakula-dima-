{pkgs}: {
  deps = [
    pkgs.xorg.xinit
    pkgs.xorg.xorgserver
    pkgs.xorg.libxcb
    pkgs.xorg.libX11
    pkgs.tk
  ];
}
