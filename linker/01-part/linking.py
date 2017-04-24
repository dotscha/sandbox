meta = {
	'name'       : "part1",
	'init'       : 0x2000,
	'start'      : 0x2003,
	'finish'     : 0x2006,
	'requires'   : ["prg1.prg","prg2.prg","data.bin@2000"],
	'reused'     : "music.sid[$7e:]@$1000",
	'uses'       : [(0x02,0xef),(0x0800,0x7fff)],
	'stack'      : 10,
	'min_length' : 20.0,
	'free_avg'   : (60,0)
}
