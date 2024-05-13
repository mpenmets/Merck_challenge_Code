# PyPlate: High-throughput Experiment Design Package

## Description
This project focuses on 2 tasks.
  1. Designing experiments for screening conditions.
  2. Conversion of binary files into csv.

### Task Q1:

This task we design experiments for screening conditions for 12 cross-coupling reactions of the form Ai + Bi → Ci. The specific experimental conditions are outlined below:

- Limiting reagent Ai: 0.1 mmol
- 1.1 equivalents of Bi per reaction
- 10 mol% Pd(OAc)2
- 15 mol% of ligand
- Total reaction volume: 200 uL
- 96 well plates with a maximum volume of 500 uL

The experiment involves 4 solvents (toluene, glyme, TBME, and dichloroethane), and 3 ligands (XPhos, SPhos, and dppf).
Design plan to use the concept of tags to add the relative quantities of substances in added in the Q1.ipynb.


### Task Q2:

The decode_data functions in the process_pear or process_scale files decodes binary data from a file and stores into CSV format, skipping specified header and trailer bytes. 
It uses struct.unpack to interpret pairs of integers and writes the decoded data to a CSV file.

#### Analysis of Pear Data:
- The pear data contains 2 values per each record. The size of each value is 4 bytes and the format used is "ii".
- This represents that each record contains 8 bytes, with 2 integers.

#### Analysis of Scale Data:
- The pear data contains 23 values per each record. The first value is a float type and remaining are signed or unsigned integers.
- Each record is represented with "fiiiiiiiiiiiiiiiiiiiiii", where each value contains 4 bytes and the record contains 92 bytes.
  
## Project Structure
- `README.md`: Overview and description of the project.
- `Q1.ipynb`: Jupyter notebook containing the PyPlate Recipe implementation for the above experimental design and proposed plan to add tags.
- `process_pear.py`: Reads and decodes binary pear data and saves it as csv.
- `process_scale.py`: Reads and decodes binary scale data and saves it as csv. 


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mpenmets/Merck_challenge_Code.git
   cd PyPlate

2. Install packages
    ```bash
    pip install pyplate-hte
    pip install numpy

3. Run Q1.ipynb notebook for task 1
4. Run below files for binary conversion task.
   ```bash
   python process_pear.py
   python process_scale.py
