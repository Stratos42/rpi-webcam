import curses,pipan

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
p = pipan.PiPan()

x = 128
y = 140

stdscr.addstr(0,0,"Hit q to quit")
stdscr.refresh()

key=''

while key != ord('q'):
	key= stdscr.getch()
	stdscr.addch(20,25,key)
	stdscr.refresh()
	if key == curses.KEY_UP:
		y = y - 1
	if key == curses.KEY_DOWN:
		y = y + 1
	if key == curses.KEY_RIGHT:
		x = x + 1
	if key == curses.KEY_LEFT:
		x = x - 1
	p.do_tilt(int(y))
	p.do_pan(int(x))

curses.endwin()
