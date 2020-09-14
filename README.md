<h1 align="center">DNA to Protein Converter</h1>
<h4 align="center">⚠️ Currently Under Development ⚠️</h4>

### Description
The aim is to take nucleotide sequences and convert them to their protein equivalent. I aim to turn this into a webapp for people to use, with multiple readout types and display options similar to what you can find on ExPASy: https://web.expasy.org/translate/

#### Non-Web Checklist
- [x] Generate Random Nucleotide Sequences
- [x] Read in Existing Sequences from text files
- [x] Generate Protein Sequence with STOP and Met indicators
- [ ] Easy Read
	- [x] Object Naming
	- [x] Nucleotide Output
	- [x] Protein Output
	- [ ] Raw Send to .txt
	- [ ] Frame Slicing
- [ ] Export as pip library for external use

#### Webapp Checklist
Developing list at the moment

#### Note:
This is written in Python so I can't swear by its ability to sequence large structures quickly (it's litterally python, what do you expect…), so try not to go over like 2M bases and you won't be waiting more than a second or two. I'm considering re-writting this in rust and then having python just call rust executables, but I'm still learning rust at the moment so it'll have to wait.
