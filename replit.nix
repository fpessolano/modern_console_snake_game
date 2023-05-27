{ pkgs }: {
	deps = [
		pkgs.sudo
    pkgs.clang_12
		pkgs.ccls
		pkgs.gdb
		pkgs.gnumake
    pkgs.ncurses
  ];
  
  env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [ pkgs.ncurses ];
}