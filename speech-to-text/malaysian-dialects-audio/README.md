pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
sudo yum install epel-release
sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum install ffmpeg ffmpeg-devel
pip install ffmpeg-python 

#using conda
conda install -c conda-forge ffmpeg

