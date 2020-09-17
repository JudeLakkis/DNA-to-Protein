from random import randint

class Sequencinator():

    def __init__(self, name=None):
        self.name = name
        self.bases = 'A T C G'.split(' ')
        self.base_opp = 'T A G C'.split(' ')
        self.nucleotide = 'Not Defined Yet'
        self.protein = 'Not Defined Yet'
        self.codon_table = {
                'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
                'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
                'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W' }

    def generate_sequence(self, seq_len=500):
        self.nucleotide= ''.join([self.bases[randint(0, len(self.bases)-1)] for i in range(seq_len)])
        return self.nucleotide

    def translate_protein(self, working_strand, file_name=None, read_external_file=None):
        # if file_name != None and (read_external_file != None and read_external_file.lower() == 'r'):
        #     with open(file_name) as f:
        #         working_strand = ''.join([i.strip() for i in f.readlines()])
        #     self.nucleotide = working_strand
        # else:
        # working_strand = self.nucleotide
        self.nucleotide = working_strand
        
        protein_chain = []
        triplet = ''
        for i in working_strand:
            if i.upper() in self.bases:
                triplet += i.upper()
            if len(triplet) == 3:
                code = self.codon_table[triplet]
                protein_chain.append(code)
                triplet = ''
        self.protein = ''.join(protein_chain)
        return self.protein

    def display(self, status=None):
        if status != None:
            pass
        else:
            # return 'Object Name: ' + str(self.name)
            print(f'Nucleotide Sequence:\n{self.nucleotide}\n\nProtein Sequence:\n{self.protein}\n\n')


# dna = Sequencinator('Randomly Generated DNA')
# dna.generate_sequence()
# dna.translate_protein(dna.nucleotide)
# dna.display()

# text_dna = Sequencinator('Text File DNA')
# text_dna.translate_protein("dna_example.txt", 'r')
# text_dna.display()

# test = Sequencinator("Test object")
# test.generate_sequence(10)
# test.translate_protein(ee)
# test.display()
