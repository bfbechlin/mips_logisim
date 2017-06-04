#!/usr/bin/python3

import sys, getopt

jump_inst = {
	'J':'000010',
	'JAL':'000011'}

imed_inst = {
	'LW':'100011', 'SW':'101011', 'BEQ':'000100',
	'SB':'10100',
# BRANCHS
	'BGEZ':'00001'}

reg_inst ={
	'ADD':'100000', 'SUB':'100010', 'AND':'100100', 'OR':'100101',
	'SLL':'000000', 'DIV':'011010'}

labelsTable = dict()

def findLabels(_file):
	lineCounter = 0;
	for line in _file:
		if ':' in line:
			line = line.strip()
			labelsTable[line.split(':')[0]] = lineCounter
		else:
			lineCounter += 1

def jump_inst_mount(line):
	itens = line.split(' ')
	inst = itens[0]
	if itens[1] in labelsTable.keys():
		return '{0}{1:026b}'.format(jump_inst[inst], labelsTable[itens[1]])
	else:
		return 0

def imed_inst_mount(line, lineCounter):
	itens = line.split(' ')
	inst = itens[0]
	rs = int(itens[1][1:])
	if (inst == 'BEQ'):
		rt = int(itens[2][1:])
		offset = labelsTable[itens[3]] - lineCounter
		print(offset)
		offset = format(offset if offset >= 0 else (1 << 16) + offset, '016b')
		if itens[3] in labelsTable.keys():
			return '{0}{1:05b}{2:05b}{3}'.format(imed_inst[inst], rs, rt, offset)
		else:
			return 0

	if(inst == 'BGEZ'):
		offset = labelsTable[itens[2]] - lineCounter
		print (offset)
		offset = format(offset if offset >= 0 else (1 << 16) + offset, '016b')
		if itens[2] in labelsTable.keys():
			return '000001{0:05b}{1}{2}'.format(rs, imed_inst[inst], offset)
		else:
			return 0

	if (inst == 'LW' or inst == 'SW' or inst == 'SB'):
		buff = itens[2].replace('(', '')
		buff = buff.replace(')', '')
		imed = int(buff.split('R')[0])
		rt = int(buff.split('R')[1])
		return '{0}{1:05b}{2:05b}{3:016b}'.format(imed_inst[inst], rt, rs, imed)

	return 0

def reg_inst_mount(line):
	itens = line.split(' ')
	inst = itens[0]
	rd = int(itens[1][1:])

	if(inst == 'SLL'):
		rt = int(itens[2][1:])
		sa = int(itens[3])
		return '00000000000{0:05b}{1:05b}{2:05b}{3}'.format(rt, rd, sa, reg_inst[inst])

	if(inst == 'ADD' or inst == 'SUB' or inst == 'AND' or inst == 'OR'):
		rs = int(itens[2][1:])
		rt = int(itens[3][1:])
		return '000000{0:05b}{1:05b}{2:05b}00000{3}'.format(rs, rt, rd, reg_inst[inst])

	return 0

def instruct_rec(_file):
	inst_list = list()
	lineCounter = 0
	for line in _file:
		line = ' '.join(line.split())
		inst = line.split(' ')[0]
		if inst in jump_inst.keys():
			inst_list.append(jump_inst_mount(line))
		elif inst in imed_inst.keys():
			inst_list.append(imed_inst_mount(line, lineCounter + 1))
		elif inst in reg_inst.keys():
			inst_list.append(reg_inst_mount(line))
		elif inst == 'NOP':
			inst_list.append('{0:032b}'.format(0))
		if(line[-1] != ':'):
			lineCounter += 1

	return inst_list

def writeAssembly(_file, assembly_list):
	_file.write('v2.0 raw\n')
	counter = 1
	for code in assembly_list:
		_file.write(format(int(code,2), 'x'))
		if counter == len(assembly_list):
			return
		if counter % 8 == 0:
			_file.write('\n')
		else:
			_file.write(' ')
		counter += 1

def main(inputFileName, outputFileName):
	inputFile = open(inputFileName, 'r')
	findLabels(inputFile)
	inputFile = open(inputFileName, 'r')
	assembly = instruct_rec(inputFile)
	print(labelsTable)
	print(assembly)
	outputFile = open(outputFileName, 'w')
	writeAssembly(outputFile, assembly)

if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])
