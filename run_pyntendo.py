from nes import NES

# Calea către ROM-ul tău NES
rom_path = "super_mario.nes"  # Înlocuiește cu fișierul tău ROM

# Creează și pornește emulatorul
nes = NES(rom_path, screen_scale=3, sync_mode=1, verbose=True)
nes.run()