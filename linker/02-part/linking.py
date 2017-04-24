meta = {
	'name'       : "part2",
	'init'       : 0x4000,
	'start'      : 0x4003,
	'finish'     : 0x4006,
	'requires'   : ["prg1.prg","prg2.prg","data.bin@$2000"],
	'reused'     : "music.sid[$7e:]@$1000",
	'uses'       : [(0x02,0xef),(0x4000,0x5fff)],
	'stack'      : 10,
	'min_length' : 20.0,
	'free_avg'   : (60,0)
}
