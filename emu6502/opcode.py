opcodes = [
	(0x00, "Implied/Stack", "BRK", 2, 7, "" ),
	(0x01, "(Indirect,X)" , "ORA", 2, 6, "" ),
	(0x02, "Implied"      , "JAM", 1, 0, "" ),
	(0x03, "(Indirect,X)" , "SLO", 2, 8, "" ),
	(0x04, "ZeroPage"     , "NOP", 2, 3, "" ),
	(0x05, "ZeroPage"     , "ORA", 2, 3, "" ),
	(0x06, "ZeroPage"     , "ASL", 2, 5, "" ),
	(0x07, "ZeroPage"     , "SLO", 2, 5, "" ),
	(0x08, "Implied/Stack", "PHP", 1, 3, "" ),
	(0x09, "Immediate"    , "ORA", 2, 2, "" ),
	(0x0A, "Accumulator"  , "ASL", 1, 2, "" ),
	(0x0B, "Immediate"    , "ANC", 2, 2, "" ),
	(0x0C, "Absolute"     , "NOP", 3, 4, "" ),
	(0x0D, "Absolute"     , "ORA", 3, 4, "" ),
	(0x0E, "Absolute"     , "ASL", 3, 6, "" ),
	(0x0F, "Absolute"     , "SLO", 3, 6, "" ),
	(0x10, "Relative"     , "BPL", 2, 2, "*"),
	(0x11, "(Indirect),Y" , "ORA", 2, 5, "*"),
	(0x12, "Implied"      , "JAM", 1, 0, "" ),
	(0x13, "(Indirect),Y" , "SLO", 2, 8, "" ),
	(0x14, "ZeroPage,X"   , "NOP", 2, 4, "" ),
	(0x15, "ZeroPage,X"   , "ORA", 2, 4, "" ),
	(0x16, "ZeroPage,X"   , "ASL", 2, 6, "" ),
	(0x17, "ZeroPage,X"   , "SLO", 2, 6, "" ),
	(0x18, "Implied"      , "CLC", 1, 2, "" ),
	(0x19, "Absolute,Y"   , "ORA", 3, 4, "*"),
	(0x1A, "Implied"      , "NOP", 1, 2, "" ),
	(0x1B, "Absolute,Y"   , "SLO", 3, 7, "" ),
	(0x1C, "Absolute,X"   , "NOP", 3, 4, "*"),
	(0x1D, "Absolute,X"   , "ORA", 3, 4, "*"),
	(0x1E, "Absolute,X"   , "ASL", 3, 7, "" ),
	(0x1F, "Absolute,X"   , "SLO", 3, 7, "" ),
	(0x20, "Absolute"     , "JSR", 3, 6, "" ),
	(0x21, "(Indirect,X)" , "AND", 2, 6, "" ),
	(0x22, "Implied"      , "JAM", 1, 0, "" ),
	(0x23, "(Indirect,X)" , "RLA", 2, 8, "" ),
	(0x24, "ZeroPage"     , "BIT", 2, 3, "" ),
	(0x25, "ZeroPage"     , "AND", 2, 3, "" ),
	(0x26, "ZeroPage"     , "ROL", 2, 5, "" ),
	(0x27, "ZeroPage"     , "RLA", 2, 5, "" ),
	(0x28, "Implied/Stack", "PLP", 1, 4, "" ),
	(0x29, "Immediate"    , "AND", 2, 2, "" ),
	(0x2A, "Accumulator"  , "ROL", 1, 2, "" ),
	(0x2B, "Immediate"    , "ANC", 2, 2, "" ),
	(0x2C, "Absolute"     , "BIT", 3, 4, "" ),
	(0x2D, "Absolute"     , "AND", 3, 4, "" ),
	(0x2E, "Absolute"     , "ROL", 3, 6, "" ),
	(0x2F, "Absolute"     , "RLA", 3, 6, "" ),
	(0x30, "Relative"     , "BMI", 2, 2, "*"),
	(0x31, "(Indirect),Y" , "AND", 2, 5, "*"),
	(0x32, "Implied"      , "JAM", 1, 0, "" ),
	(0x33, "(Indirect),Y" , "RLA", 2, 8, "" ),
	(0x34, "ZeroPage,X"   , "NOP", 2, 4, "" ),
	(0x35, "ZeroPage,X"   , "AND", 2, 4, "" ),
	(0x36, "ZeroPage,X"   , "ROL", 2, 6, "" ),
	(0x37, "ZeroPage,X"   , "RLA", 2, 6, "" ),
	(0x38, "Implied"      , "SEC", 1, 2, "" ),
	(0x39, "Absolute,Y"   , "AND", 3, 4, "*"),
	(0x3A, "Implied"      , "NOP", 1, 2, "" ),
	(0x3B, "Absolute,Y"   , "RLA", 3, 7, "" ),
	(0x3C, "Absolute,X"   , "NOP", 3, 4, "*"),
	(0x3D, "Absolute,X"   , "AND", 3, 4, "*"),
	(0x3E, "Absolute,X"   , "ROL", 3, 7, "" ),
	(0x3F, "Absolute,X"   , "RLA", 3, 7, "" ),
	(0x40, "Implied/Stack", "RTI", 1, 6, "" ),
	(0x41, "(Indirect,X)" , "EOR", 2, 6, "" ),
	(0x42, "Implied"      , "JAM", 1, 0, "" ),
	(0x43, "(Indirect,X)" , "SRE", 2, 8, "" ),
	(0x44, "ZeroPage"     , "NOP", 2, 3, "" ),
	(0x45, "ZeroPage"     , "EOR", 2, 3, "" ),
	(0x46, "ZeroPage"     , "LSR", 2, 5, "" ),
	(0x47, "ZeroPage"     , "SRE", 2, 5, "" ),
	(0x48, "Implied/Stack", "PHA", 1, 3, "" ),
	(0x49, "Immediate"    , "EOR", 2, 2, "" ),
	(0x4A, "Accumulator"  , "LSR", 1, 2, "" ),
	(0x4B, "Immediate"    , "ASR", 2, 2, "" ),
	(0x4C, "Absolute"     , "JMP", 3, 3, "" ),
	(0x4D, "Absolute"     , "EOR", 3, 4, "" ),
	(0x4E, "Absolute"     , "LSR", 3, 6, "" ),
	(0x4F, "Absolute"     , "SRE", 3, 6, "" ),
	(0x50, "Relative"     , "BVC", 2, 2, "*"),
	(0x51, "(Indirect),Y" , "EOR", 2, 5, "*"),
	(0x52, "Implied"      , "JAM", 1, 0, "" ),
	(0x53, "(Indirect),Y" , "SRE", 2, 8, "" ),
	(0x54, "ZeroPage,X"   , "NOP", 2, 4, "" ),
	(0x55, "ZeroPage,X"   , "EOR", 2, 4, "" ),
	(0x56, "ZeroPage,X"   , "LSR", 2, 6, "" ),
	(0x57, "ZeroPage,X"   , "SRE", 2, 6, "" ),
	(0x58, "Implied"      , "CLI", 1, 2, "" ),
	(0x59, "Absolute,Y"   , "EOR", 3, 4, "*"),
	(0x5A, "Implied"      , "NOP", 1, 2, "" ),
	(0x5B, "Absolute,Y"   , "SRE", 3, 7, "" ),
	(0x5C, "Absolute,X"   , "NOP", 3, 4, "*"),
	(0x5D, "Absolute,X"   , "EOR", 3, 4, "*"),
	(0x5E, "Absolute,X"   , "LSR", 3, 7, "" ),
	(0x5F, "Absolute,X"   , "SRE", 3, 7, "" ),
	(0x60, "Implied/Stack", "RTS", 1, 6, "" ),
	(0x61, "(Indirect,X)" , "ADC", 2, 6, "" ),
	(0x62, "Implied"      , "JAM", 1, 0, "" ),
	(0x63, "(Indirect,X)" , "RRA", 2, 8, "" ),
	(0x64, "ZeroPage"     , "NOP", 2, 3, "" ),
	(0x65, "ZeroPage"     , "ADC", 2, 3, "" ),
	(0x66, "ZeroPage"     , "ROR", 2, 5, "" ),
	(0x67, "ZeroPage"     , "RRA", 2, 5, "" ),
	(0x68, "Implied/Stack", "PLA", 1, 4, "" ),
	(0x69, "Immediate"    , "ADC", 2, 2, "" ),
	(0x6A, "Accumulator"  , "ROR", 1, 2, "" ),
	(0x6B, "Immediate"    , "ARR", 2, 2, "" ),
	(0x6C,"(Abs.Indirect)", "JMP", 3, 5, "" ),
	(0x6D, "Absolute"     , "ADC", 3, 4, "" ),
	(0x6E, "Absolute"     , "ROR", 3, 6, "" ),
	(0x6F, "Absolute"     , "RRA", 3, 6, "" ),
	(0x70, "Relative"     , "BVS", 2, 2, "*"),
	(0x71, "(Indirect),Y" , "ADC", 2, 5, "*"),
	(0x72, "Implied"      , "JAM", 1, 0, "" ),
	(0x73, "(Indirect),Y" , "RRA", 2, 8, "" ),
	(0x74, "ZeroPage,X"   , "NOP", 2, 4, "" ),
	(0x75, "ZeroPage,X"   , "ADC", 2, 4, "" ),
	(0x76, "ZeroPage,X"   , "ROR", 2, 6, "" ),
	(0x77, "ZeroPage,X"   , "RRA", 2, 6, "" ),
	(0x78, "Implied"      , "SEI", 1, 2, "" ),
	(0x79, "Absolute,Y"   , "ADC", 3, 4, "*"),
	(0x7A, "Implied"      , "NOP", 1, 2, "" ),
	(0x7B, "Absolute,Y"   , "RRA", 3, 7, "" ),
	(0x7C, "Absolute,X"   , "NOP", 3, 4, "*"),
	(0x7D, "Absolute,X"   , "ADC", 3, 4, "*"),
	(0x7E, "Absolute,X"   , "ROR", 3, 7, "" ),
	(0x7F, "Absolute,X"   , "RRA", 3, 7, "" ),
	(0x80, "Immediate"    , "NOP", 2, 2, "" ),
	(0x81, "(Indirect,X)" , "STA", 2, 6, "" ),
	(0x82, "Immediate"    , "NOP", 2, 2, "" ),
	(0x83, "(Indirect,X)" , "SAX", 2, 6, "" ),
	(0x84, "ZeroPage"     , "STY", 2, 3, "" ),
	(0x85, "ZeroPage"     , "STA", 2, 3, "" ),
	(0x86, "ZeroPage"     , "STX", 2, 3, "" ),
	(0x87, "ZeroPage"     , "SAX", 2, 3, "" ),
	(0x88, "Implied"      , "DEY", 1, 2, "" ),
	(0x89, "Immediate"    , "NOP", 2, 2, "" ),
	(0x8A, "Implied"      , "TXA", 1, 2, "" ),
	(0x8B, "Immediate"    , "ANE", 2, 2, "" ),
	(0x8C, "Absolute"     , "STY", 3, 4, "" ),
	(0x8D, "Absolute"     , "STA", 3, 4, "" ),
	(0x8E, "Absolute"     , "STX", 3, 4, "" ),
	(0x8F, "Absolute"     , "SAX", 3, 4, "" ),
	(0x90, "Relative"     , "BCC", 2, 2, "*"),
	(0x91, "(Indirect),Y" , "STA", 2, 6, "" ),
	(0x92, "Implied"      , "JAM", 1, 0, "" ),
	(0x93, "Absolute,X"   , "SHA", 3, 5, "" ),
	(0x94, "ZeroPage,X"   , "STY", 2, 4, "" ),
	(0x95, "ZeroPage,X"   , "STA", 2, 4, "" ),
	(0x96, "ZeroPage,Y"   , "STX", 2, 4, "" ),
	(0x97, "ZeroPage,Y"   , "SAX", 2, 4, "" ),
	(0x98, "Implied"      , "TYA", 1, 2, "" ),
	(0x99, "Absolute,Y"   , "STA", 3, 5, "" ),
	(0x9A, "Implied"      , "TXS", 1, 2, "" ),
	(0x9B, "Absolute,Y"   , "SHS", 3, 5, "" ),
	(0x9C, "Absolute,X"   , "SHY", 3, 5, "" ),
	(0x9D, "Absolute,X"   , "STA", 3, 5, "" ),
	(0x9E, "Absolute,Y"   , "SHX", 3, 5, "" ),
	(0x9F, "Absolute,Y"   , "SHA", 3, 5, "" ),
	(0xA0, "Immediate"    , "LDY", 2, 2, "" ),
	(0xA1, "(Indirect,X)" , "LDA", 2, 6, "" ),
	(0xA2, "Immediate"    , "LDX", 2, 2, "" ),
	(0xA3, "(Indirect,X)" , "LAX", 2, 6, "" ),
	(0xA4, "ZeroPage"     , "LDY", 2, 3, "" ),
	(0xA5, "ZeroPage"     , "LDA", 2, 3, "" ),
	(0xA6, "ZeroPage"     , "LDX", 2, 3, "" ),
	(0xA7, "ZeroPage"     , "LAX", 2, 3, "" ),
	(0xA8, "Implied"      , "TAY", 1, 2, "" ),
	(0xA9, "Immediate"    , "LDA", 2, 2, "" ),
	(0xAA, "Implied"      , "TAX", 1, 2, "" ),
	(0xAB, "Immediate"    , "LXA", 2, 2, "" ),
	(0xAC, "Absolute"     , "LDY", 3, 4, "" ),
	(0xAD, "Absolute"     , "LDA", 3, 4, "" ),
	(0xAE, "Absolute"     , "LDX", 3, 4, "" ),
	(0xAF, "Absolute"     , "LAX", 3, 4, "" ),
	(0xB0, "Relative"     , "BCS", 2, 2, "*"),
	(0xB1, "(Indirect),Y" , "LDA", 2, 5, "*"),
	(0xB2, "Implied"      , "JAM", 1, 0, "" ),
	(0xB3, "(Indirect),Y" , "LAX", 2, 5, "*"),
	(0xB4, "ZeroPage,X"   , "LDY", 2, 4, "" ),
	(0xB5, "ZeroPage,X"   , "LDA", 2, 4, "" ),
	(0xB6, "ZeroPage,Y"   , "LDX", 2, 4, "" ),
	(0xB7, "ZeroPage,Y"   , "LAX", 2, 4, "" ),
	(0xB8, "Implied"      , "CLV", 1, 2, "" ),
	(0xB9, "Absolute,Y"   , "LDA", 3, 4, "*"),
	(0xBA, "Implied"      , "TSX", 1, 2, "" ),
	(0xBB, "Absolute,Y"   , "LAE", 3, 4, "*"),
	(0xBC, "Absolute,X"   , "LDY", 3, 4, "*"),
	(0xBD, "Absolute,X"   , "LDA", 3, 4, "*"),
	(0xBE, "Absolute,Y"   , "LDX", 3, 4, "*"),
	(0xBF, "Absolute,Y"   , "LAX", 3, 4, "*"),
	(0xC0, "Immediate"    , "CPY", 2, 2, "" ),
	(0xC1, "(Indirect,X)" , "CMP", 2, 6, "" ),
	(0xC2, "Immediate"    , "NOP", 2, 2, "" ),
	(0xC3, "(Indirect,X)" , "DCP", 2, 8, "" ),
	(0xC4, "ZeroPage"     , "CPY", 2, 3, "" ),
	(0xC5, "ZeroPage"     , "CMP", 2, 3, "" ),
	(0xC6, "ZeroPage"     , "DEC", 2, 5, "" ),
	(0xC7, "ZeroPage"     , "DCP", 2, 5, "" ),
	(0xC8, "Implied"      , "INY", 1, 2, "" ),
	(0xC9, "Immediate"    , "CMP", 2, 2, "" ),
	(0xCA, "Implied"      , "DEX", 1, 2, "" ),
	(0xCB, "Immediate"    , "SBX", 2, 2, "" ),
	(0xCC, "Absolute"     , "CPY", 3, 4, "" ),
	(0xCD, "Absolute"     , "CMP", 3, 4, "" ),
	(0xCE, "Absolute"     , "DEC", 3, 6, "" ),
	(0xCF, "Absolute"     , "DCP", 3, 6, "" ),
	(0xD0, "Relative"     , "BNE", 2, 2, "*"),
	(0xD1, "(Indirect),Y" , "CMP", 2, 5, "*"),
	(0xD2, "Implied"      , "JAM", 1, 0, "" ),
	(0xD3, "(Indirect),Y" , "DCP", 2, 8, "" ),
	(0xD4, "ZeroPage,X"   , "NOP", 2, 4, "" ),
	(0xD5, "ZeroPage,X"   , "CMP", 2, 4, "" ),
	(0xD6, "ZeroPage,X"   , "DEC", 2, 6, "" ),
	(0xD7, "ZeroPage,X"   , "DCP", 2, 6, "" ),
	(0xD8, "Implied"      , "CLD", 1, 2, "" ),
	(0xD9, "Absolute,Y"   , "CMP", 3, 4, "*"),
	(0xDA, "Implied"      , "NOP", 1, 2, "" ),
	(0xDB, "Absolute,Y"   , "DCP", 3, 7, "" ),
	(0xDC, "Absolute,X"   , "NOP", 3, 4, "*"),
	(0xDD, "Absolute,X"   , "CMP", 3, 4, "*"),
	(0xDE, "Absolute,X"   , "DEC", 3, 7, "" ),
	(0xDF, "Absolute,X"   , "DCP", 3, 7, "" ),
	(0xE0, "Immediate"    , "CPX", 2, 2, "" ),
	(0xE1, "(Indirect,X)" , "SBC", 2, 6, "" ),
	(0xE2, "Immediate"    , "NOP", 2, 2, "" ),
	(0xE3, "(Indirect,X)" , "ISB", 2, 8, "" ),
	(0xE4, "ZeroPage"     , "CPX", 2, 3, "" ),
	(0xE5, "ZeroPage"     , "SBC", 2, 3, "" ),
	(0xE6, "ZeroPage"     , "INC", 2, 5, "" ),
	(0xE7, "ZeroPage"     , "ISB", 2, 5, "" ),
	(0xE8, "Implied"      , "INX", 1, 2, "" ),
	(0xE9, "Immediate"    , "SBC", 2, 2, "" ),
	(0xEA, "Implied"      , "NOP", 1, 2, "" ),
	(0xEB, "Immediate"    , "SBC", 2, 2, "" ),
	(0xEC, "Absolute"     , "CPX", 3, 4, "" ),
	(0xED, "Absolute"     , "SBC", 3, 4, "" ),
	(0xEE, "Absolute"     , "INC", 3, 6, "" ),
	(0xEF, "Absolute"     , "ISB", 3, 6, "" ),
	(0xF0, "Relative"     , "BEQ", 2, 2, "*"),
	(0xF1, "(Indirect),Y" , "SBC", 2, 5, "*"),
	(0xF2, "Implied"      , "JAM", 1, 0, "" ),
	(0xF3, "(Indirect),Y" , "ISB", 2, 8, "" ),
	(0xF4, "ZeroPage,X"   , "NOP", 2, 4, "" ),
	(0xF5, "ZeroPage,X"   , "SBC", 2, 4, "" ),
	(0xF6, "ZeroPage,X"   , "INC", 2, 6, "" ),
	(0xF7, "ZeroPage,X"   , "ISB", 2, 6, "" ),
	(0xF8, "Implied"      , "SED", 1, 2, "" ),
	(0xF9, "Absolute,Y"   , "SBC", 3, 4, "*"),
	(0xFA, "Implied"      , "NOP", 1, 2, "" ),
	(0xFB, "Absolute,Y"   , "ISB", 3, 7, "" ),
	(0xFC, "Absolute,X"   , "NOP", 3, 4, "*"),
	(0xFD, "Absolute,X"   , "SBC", 3, 4, "*"),
	(0xFE, "Absolute,X"   , "INC", 3, 7, "" ),
	(0xFF, "Absolute,X"   , "ISB", 3, 7, "" )
]
