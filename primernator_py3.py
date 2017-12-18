#!/usr/bin/env python

from tkinter import *
import math as math

class ABC(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

root = Tk()
app = ABC(master=root)
app.master.title("The Prime(r)nator")

tk_product_min=IntVar()
tk_product_max=IntVar()
tk_min_length=IntVar()
tk_max_length=IntVar()
tk_min_Tm=DoubleVar()
tk_max_Tm=DoubleVar()
tk_Tm_diff=DoubleVar()
tk_min_GC=DoubleVar()
tk_max_GC=DoubleVar()
tk_first=BooleanVar()
tk_last=BooleanVar()
tk_last_6=IntVar()
tk_rep_check=BooleanVar()
tk_repetition=IntVar()
tk_salt_conc=DoubleVar()

tk_min_length.set(19)
tk_max_length.set(22)
tk_min_Tm.set(55.0)
tk_max_Tm.set(65.0)
tk_Tm_diff.set(5.0)
tk_min_GC.set(40.0)
tk_max_GC.set(60.0)
tk_first.set(False)
tk_last.set(True)
tk_last_6.set(3)
tk_rep_check.set(True)
tk_repetition.set(4)
tk_salt_conc.set(1.0)

Total = Frame(root)
Total.pack()
L_total_seq = Label(Total, text="Enter Full Sequence:")
L_total_seq.pack(side = LEFT)
total_seq = Entry(Total, width=75)
total_seq.pack(side = LEFT)

Forward = Frame(root)
Forward.pack()
L_forward_region = Label(Forward, text="Enter F-Primer Region:")
L_forward_region.pack(side = LEFT)
forward_region = Entry(Forward, width=75)
forward_region.pack(side = LEFT)

Reverse = Frame(root)
Reverse.pack()
L_reverse_region = Label(Reverse, text="Enter R-Primer Region:")
L_reverse_region.pack(side = LEFT)
reverse_region = Entry(Reverse, width=75)
reverse_region.pack(side = LEFT)

Min_Max = Frame(root)
Min_Max.pack()
L_min_size = Label(Min_Max, text="Enter Min Product Size:")
L_min_size.pack(side = LEFT)
min_size = Entry(Min_Max, textvariable=tk_product_min, width=25)
min_size.pack(side = LEFT)
L_max_size = Label(Min_Max, text="Enter Max Product Size:")
L_max_size.pack(side = LEFT)
max_size = Entry(Min_Max, textvariable=tk_product_max, width=25)
max_size.pack(side = LEFT)

out=StringVar()
output_frame = Frame(root)
output_frame.pack()
output=Text(output_frame, height=50, width=100, wrap=WORD)
output.pack()

def settings_menu():
	menu=Toplevel()

	Primer_Length = Frame(menu, width=50)
	Primer_Length.pack()
	Length_Min_Label = Label(Primer_Length, text="Primer Length-- Min:")
	Length_Min_Label.pack(side = LEFT)
	Length_min = Entry(Primer_Length, textvariable=tk_min_length, width=10)
	Length_min.pack(side = LEFT)
	Length_Max_Label = Label(Primer_Length, text="Max:")
	Length_Max_Label.pack(side = LEFT)
	Length_max = Entry(Primer_Length, textvariable=tk_max_length, width=10)
	Length_max.pack(side = LEFT)

	Tm = Frame(menu, width=50)
	Tm.pack()
	Tm_Min_Label = Label(Tm, text="Tm-- Min:")
	Tm_Min_Label.pack(side = LEFT)
	Tm_min = Entry(Tm, textvariable=tk_min_Tm, width=10)
	Tm_min.pack(side = LEFT)
	Tm_Max_Label = Label(Tm, text="Max:")
	Tm_Max_Label.pack(side = LEFT)
	Tm_max = Entry(Tm, textvariable=tk_max_Tm, width=10)
	Tm_max.pack(side = LEFT)

	Tm_Diff = Frame(menu, width=50)
	Tm_Diff.pack()
	Tm_diff_Label = Label(Tm_Diff, text="Max Tm Difference:")
	Tm_diff_Label.pack(side = LEFT)
	Tm_diff_entry = Entry(Tm_Diff, textvariable=tk_Tm_diff, width=10)
	Tm_diff_entry.pack(side = LEFT)

	GC = Frame(menu, width=50)
	GC.pack()
	GC_Min_Label = Label(GC, text="GC content-- Min:")
	GC_Min_Label.pack(side = LEFT)
	GC_min = Entry(GC, textvariable=tk_min_GC, width=10)
	GC_min.pack(side = LEFT)
	GC_Max_Label = Label(GC, text="Max:")
	GC_Max_Label.pack(side = LEFT)
	GC_max = Entry(GC, textvariable=tk_max_GC, width=10)
	GC_max.pack(side = LEFT)

	first_base = Frame(menu, width=50)
	first_base.pack()
	first_base_label = Label(first_base, text="First base must be A or T:")
	first_base_label.pack(side = LEFT)
	first_base_on = Radiobutton(first_base, text="On", variable=tk_first, value=True)
	first_base_on.pack(side = LEFT)
	first_base_off = Radiobutton(first_base, text="Off", variable=tk_first, value=False)
	first_base_off.pack(side = LEFT)

	last_base = Frame(menu, width=50)
	last_base.pack()
	last_base_label = Label(last_base, text="Last base must be G or C:")
	last_base_label.pack(side = LEFT)
	last_base_on = Radiobutton(last_base, text="On", variable=tk_last, value=True)
	last_base_on.pack(side = LEFT)
	last_base_off = Radiobutton(last_base, text="Off", variable=tk_last, value=False)
	last_base_off.pack(side = LEFT)

	Avoid_Rep = Frame(menu, width=50)
	Avoid_Rep.pack()
	Avoid_Rep_label = Label(Avoid_Rep, text="Avoid Repetition:")
	Avoid_Rep_label.pack(side = LEFT)
	Avoid_Rep_on = Radiobutton(Avoid_Rep, text="On", variable=tk_rep_check, value=1)
	Avoid_Rep_on.pack(side = LEFT)
	Avoid_Rep_off = Radiobutton(Avoid_Rep, text="Off", variable=tk_rep_check, value=0)
	Avoid_Rep_off.pack(side = LEFT)
	Avoid_Rep_entry_label = Label(Avoid_Rep, text="Define 'repetitive':")
	Avoid_Rep_entry_label.pack(side = LEFT)
	Avoid_Rep_entry = Entry(Avoid_Rep, textvariable=tk_repetition, width=10)
	Avoid_Rep_entry.pack(side = LEFT)
	Avoid_Rep_base_label = Label(Avoid_Rep, text="bases")
	Avoid_Rep_base_label.pack(side = LEFT)

	GCs_last6 = Frame(menu, width=50)
	GCs_last6.pack()
	GCs_last6_label = Label(GCs_last6, text="# G or C in last 6 bases:")
	GCs_last6_label.pack(side = LEFT)
	GCs_last6_entry = Entry(GCs_last6, textvariable=tk_last_6, width=10)
	GCs_last6_entry.pack(side = LEFT)

	Salt_Conc = Frame(menu, width=50)
	Salt_Conc.pack()
	salt_conc_label = Label(Salt_Conc, text="Salt concentration:")
	salt_conc_label.pack(side = LEFT)
	salt_conc_entry = Entry(Salt_Conc, textvariable=tk_salt_conc, width=10)
	salt_conc_entry.pack(side = LEFT)
	
	def exit_settings():
		menu.destroy()

	def default():
		tk_min_length.set(19)
		tk_max_length.set(22)
		tk_min_Tm.set(55.0)
		tk_max_Tm.set(65.0)
		tk_Tm_diff.set(5.0)
		tk_min_GC.set(40.0)
		tk_max_GC.set(60.0)
		tk_first.set(False)
		tk_last.set(True)
		tk_last_6.set(3)
		tk_rep_check.set(True)
		tk_repetition.set(4)

	Buttons_frame= Frame(menu, width=50)
	Buttons_frame.pack()

	default_button = Button(Buttons_frame, text="Restore Defaults", width=15, command=default)
	default_button.pack(side=LEFT)

	settings_quit_button = Button(Buttons_frame, text="SAVE & QUIT", width=10, command=exit_settings)
	settings_quit_button.pack(side=LEFT)

def callback():

	final=""
	full_sequence = str(total_seq.get())

	start = str(forward_region.get())
	if start == '':
		start=full_sequence
		final=final+"--No forward region specified, forward region set as full sequence--\n"

	end = str(reverse_region.get())
	if end == '':
		end=full_sequence
		final=final+"--No reverse region specified, reverse region set as full sequence--\n"

	size_min=int(tk_product_min.get())


	if tk_product_max.get() == 0 :
		size_max=100000000000000000000
		final=final+"--Product size must be bigger than 0, set to 10x10^20--\n"
	else:
		size_max=(tk_product_max.get())

	if type(tk_min_length.get()) in (int, float):
		min_length=int(tk_min_length.get())
	else:
		min_length=19
		final=final+"--Invalid minimum primer length, reset to default of 19--\n"

	if type(tk_max_length.get()) in (int, float):
		max_length=int(tk_max_length.get())
	else:
		max_length=22
		final=final+"--Invalid maximum primer length, reset to default of 22--\n"

	if type(tk_min_Tm.get()) in (int, float):
		min_Tm=float(tk_min_Tm.get())
	else:
		min_Tm=55.0
		final=final+"--Invalid minimum Tm, reset to default of 55.0 C--\n"

	if type(tk_min_Tm.get()) in (int, float):
		max_Tm=float(tk_max_Tm.get())
	else:
		max_Tm=65.0
		final=final+"--Invalid maximum Tm, reset to default of 65.0 C--\n"

	if type(tk_Tm_diff.get()) in (int, float):
		Tm_diff=float(tk_Tm_diff.get())
	else:
		Tm_diff=5.0
		final=final+"--Invalid maximum Tm difference, reset to default of 5.0 C--\n"

	if type(tk_min_GC.get()) in (int, float):
		min_GC=float(tk_min_GC.get())
	else:
		min_GC=40.0
		final=final+"--Invalid minimum GC content, reset to default of 40.0%--\n"

	if type(tk_max_GC.get()) in (int, float):
		max_GC=float(tk_max_GC.get())
	else:
		max_GC=60.0
		final=final+"--Invalid maximum GC content, reset to default of 60.0%--\n"

	first=tk_first.get()
	last=tk_last.get()

	if type(tk_last_6.get()) in (int, float) and 6 >= int(tk_last_6.get()) >= 0:
		last_6=int(tk_last_6.get())
	else:
		last_6=3
		final=final+"--Invalid # of GC's in last 6 bases, reset to default of 3--\n"

	rep_check=tk_rep_check.get()

	if type(tk_repetition.get()) in (int, float):
		repetition=int(tk_repetition.get())
	else:
		repetition=4
		final=final+"Invalid repetition setting, reset to default of 4 consecutive bases\n"
		
	if type(tk_salt_conc.get()) in (int, float):
		salt_conc=int(tk_salt_conc.get())
	else:
		salt_conc=1
		final=final+"Invalid salt concentration setting, reset to default of 1M NaCl\n"

	################################################################################
	########################LOOK FOR FORWARD PRIMERS################################
	################################################################################

	primer_forward_list=[] #make empty list to fill with primers that pass user-defined settings
	for x in range(min_length,(max_length+1)): #look for every possible sequence that meets length requirements
		for y in range(0,len(start)-x+1): #look in desired exon/feature
			Fprimer=start[y:(y+x)]#slice the primer sequence in question

			GC_content=(float(Fprimer.count('G')+Fprimer.count('C'))/float(len(Fprimer)))*100 #calculate GC%

			dH=0.0 #value for enthalpy
			dS=(.368*(len(Fprimer)-1)*-2.99573227355) #value of entropy
			for z in range(0,len(Fprimer)-1): #loops calculates entropy and enthalpy of sequences provided for calculating Tm
				if Fprimer[z:(z+2)] in ('AA','TT'):
					dH=dH-7900.0
					dS=dS-22.2
				elif Fprimer[z:(z+2)] in ('AT'):
					dH=dH-7200.0
					dS=dS-20.4
				elif Fprimer[z:(z+2)] in ('TA'):
					dH=dH-7200.0
					dS=dS-21.3
				elif Fprimer[z:(z+2)] in ('CA','TG'):
					dH=dH-8500.0
					dS=dS-22.7
				elif Fprimer[z:(z+2)] in ('GT','AC'):
					dH=dH-8400.0
					dS=dS-22.4
				elif Fprimer[z:(z+2)] in ('CT','AG'):
					dH=dH-7800.0
					dS=dS-21.0
				elif Fprimer[z:(z+2)] in ('GA','TC'):
					dH=dH-8200.0
					dS=dS-22.2
				elif Fprimer[z:(z+2)] in ('CG'):
					dH=dH-10600.0
					dS=dS-27.2
				elif Fprimer[z:(z+2)] in ('GC'):
					dH=dH-9800.0
					dS=dS-24.4
				elif Fprimer[z:(z+2)] in ('GG','CC'):
					dH=dH-8000.0
					dS=dS-19.9
				else:
					pass
			
			dS=dS+(.368*(len(Fprimer)-1)*math.log(salt_conc))
			Tm=(dH/(dS+1.987*-16.8112428315))-273.15 #calculate Tm

			GC_last6= Fprimer[-6:].count('G')+Fprimer[-6:].count('C') #calculate G/C's at 3' end of sequence

			if first == True : #if checking for 5' A/T is enabled, check the sequence and store a boolean to record whether it passed or not
				if Fprimer[0] in ('A','T') :
					first_pass=True
				else :
					first_pass=False
			else :
				first_pass=True #otherwise pass is automatically

			if last == True : #if checking for 3' G/C is enabled, check the sequence and store a boolean to record whether it passed or not
				if Fprimer[-1] in ('G','C') :
					last_pass=True
				else :
					last_pass=False
			else :
				last_pass=True #otherwise pass is automatically

			if rep_check == True : #if checking for repetition is enabled, check the sequence and store a boolean to record whether it passed or not
				if ('A'*repetition) in Fprimer or ('T'*repetition) in Fprimer or ('G'*repetition) in Fprimer or ('C'*repetition) in Fprimer :
					rep_pass = False
				else :
					rep_pass = True
			else:
				rep_pass = True #otherwise pass is automatically

			Instances=full_sequence.count(Fprimer)

			if (max_GC >= GC_content >= min_GC and max_Tm >= Tm >= min_Tm and GC_last6 >= last_6 and first_pass==True and last_pass==True and rep_pass==True and Instances==1): #If the primer meets all criteria, add it to the forward primer list
				primer_forward_list.append([Fprimer,len(Fprimer),round(GC_content, 2),round(Tm, 2)])

	final=final+("\nFound {} eligible forward primers.\n".format(len(primer_forward_list)))


	################################################################################
	########################LOOK FOR REVERSE PRIMERS################################
	########  This code is much the same as the previous for-loop  #################
	################################################################################

	primer_reverse_list=[]
	for x in range(min_length,(max_length+1)):
		for y in range(0,len(end)-x+1):
			Rprimer=end[y:(y+x)]

			GC_content=(float(Rprimer.count('G')+Rprimer.count('C'))/float(len(Rprimer)))*100

			dH=0.0
			dS=(.368*(len(Rprimer)-1)*-2.99573227355)
			for z in range(0,len(Rprimer)-1):
				if Rprimer[z:(z+2)] in ('AA','TT'):
					dH=dH-7900.0
					dS=dS-22.2
				elif Rprimer[z:(z+2)] in ('AT'):
					dH=dH-7200.0
					dS=dS-20.4
				elif Rprimer[z:(z+2)] in ('TA'):
					dH=dH-7200.0
					dS=dS-21.3
				elif Rprimer[z:(z+2)] in ('CA','TG'):
					dH=dH-8500.0
					dS=dS-22.7
				elif Rprimer[z:(z+2)] in ('GT','AC'):
					dH=dH-8400.0
					dS=dS-22.4
				elif Rprimer[z:(z+2)] in ('CT','AG'):
					dH=dH-7800.0
					dS=dS-21.0
				elif Rprimer[z:(z+2)] in ('GA','TC'):
					dH=dH-8200.0
					dS=dS-22.2
				elif Rprimer[z:(z+2)] in ('CG'):
					dH=dH-10600.0
					dS=dS-27.2
				elif Rprimer[z:(z+2)] in ('GC'):
					dH=dH-9800.0
					dS=dS-24.4
				elif Rprimer[z:(z+2)] in ('GG','CC'):
					dH=dH-8000.0
					dS=dS-19.9
				else:
					pass
			
			dS=dS+(.368*(len(Rprimer)-1)*math.log(salt_conc))
			Tm=(dH/(dS+1.987*-16.8112428315))-273.15

			#Since these are reverse primers, the meaning of 5' and 3' changes so the coordinates for checking bases on the ends are reversed

			GC_last6= Rprimer[:6].count('G')+Rprimer[:6].count('C')

			if first == True :
				if Rprimer[-1] in ('A','T') :
					first_pass=True
				else :
					first_pass=False
			else :
				first_pass=True

			if last == True :
				if Rprimer[0] in ('G','C') :
					last_pass=True
				else :
					last_pass=False
			else :
				last_pass=True

			if rep_check == True :
				if ('A'*repetition) in Rprimer or ('T'*repetition) in Rprimer or ('G'*repetition) in Rprimer or ('C'*repetition) in Rprimer :
					rep_pass = False
				else :
					rep_pass = True
			else :
				rep_pass = True

			Instances=full_sequence.count(Rprimer)

			if (max_GC >= GC_content >= min_GC and max_Tm >= Tm >= min_Tm and GC_last6 >= last_6 and first_pass==True and last_pass==True and rep_pass==True and Instances==1): #If the primer meets all criteria, add it to the reverse primer list
				primer_reverse_list.append([Rprimer,len(Rprimer),round(GC_content, 2),round(Tm, 2)])

	final=final+("Found {} eligible reverse primers.\n\n".format(len(primer_reverse_list)))

	#################################################################
	###############CREATE PRIMER PAIRS###############################
	#################################################################

	f_counter=0 #counter for how many times the first for loop has run for locating information of primers in forward_primer_list
	candidates=[]

	for primer1 in (i[0] for i in primer_forward_list): #locate sequence of primer in question
		r_counter=0 #counter for locating reverse primers in original list
		for primer2 in (i[0] for i in primer_reverse_list):
			reverse_complement=''
			bp_length=(full_sequence.rfind(primer2)+len(primer2)-full_sequence.find(primer1)) #calculate the length of the product formula (index of reverse primer)-(index of forward primer)+(length of primer2, since the index of the reverse primers is only the first base)
			if (size_max >= bp_length >= size_min and (primer_forward_list[f_counter][3]-primer_reverse_list[r_counter][3]) < Tm_diff): #if the product is of the right size, and the primers are within a good melting temperature range of each other
					for rc in reversed(range(-(len(primer2)),0)): #create the reverse complement of the reverse primer for user's sake
						if primer2[rc] == 'A':
							reverse_complement=reverse_complement+'T'
						elif primer2[rc] == 'T':
							reverse_complement=reverse_complement+'A'
						elif primer2[rc] == 'G':
							reverse_complement=reverse_complement+'C'
						elif primer2[rc] == 'C':
							reverse_complement=reverse_complement+'G'
					candidates.append([primer_forward_list[f_counter],[reverse_complement,primer_reverse_list[r_counter][1],primer_reverse_list[r_counter][2],primer_reverse_list[r_counter][3]],bp_length]) #add all relevant information of primer pair to list
			r_counter=r_counter+1
		f_counter=f_counter+1

	###################################################################
	######################PRINT OUTPUT#################################
	###################################################################

	def calculate_Tm_diff(list):
		return abs(list[0][3] - list[1][3]) #calculate Tm difference of forward and reverse primers for sorting

	candidates.sort(key=calculate_Tm_diff) #sort primer pairs by how similar the Tm values are

	output_counter=1
	if len(candidates) >= 10 :
		final=final+("Top 10 primer combos displayed below:\n\n  	[Sequence, Primer Length, GC%, Tm, Product Length]\n")
		for set in range(0,10):
			final= final + "{}:	Forward:{}, {}\n 	Reverse:{}\n\n".format(output_counter,candidates[set][0],candidates[set][2],candidates[set][1])
			output_counter=output_counter+1
	elif len(candidates) < 10 :
		final=final+("Only {} primer combinations found:\n\n  	[Sequence, Primer Length, GC%, Tm, Product Length]\n".format(len(candidates)))
		for set in candidates:
				final= final + "{}:	Forward:{}, {}\n 	Reverse:{}\n\n".format(output_counter,set[0],set[2],set[1])
				output_counter=output_counter+1

	out.set(final)
	output.insert(END, out.get())

def clear():
	output.delete('1.0', END)

get_primers_button = Button(root, text="Get Primers", width=10, command=callback)
get_primers_button.pack(side=LEFT)

clear_button = Button(root, text="Clear Results", command=clear)
clear_button.pack(side=LEFT)

settings_button = Button(root, text="SETTINGS", command=settings_menu)
settings_button.pack(side=LEFT)

quit_button = Button(root, text="QUIT", width=10, command=root.quit)
quit_button.pack(side=LEFT)

mainloop()
