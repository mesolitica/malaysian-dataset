git clone https://github.com/robertostling/eflomal.git
cd eflomal
make
make install -e INSTALLDIR=~/bin
python3 setup.py install --user

git clone https://github.com/clab/fast_align.git
cd fast_align
mkdir build
cd build
cmake ..
make

git clone https://github.com/moses-smt/mosesdecoder.git