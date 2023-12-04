# Ultrachat like using Malaysian context

Prepare multiturn dialogue between user and assistant for malaysian context,
1. Astroawani, https://huggingface.co/datasets/malaysia-ai/crawl-astroawani
2. Crossref `melayu` papers, https://huggingface.co/datasets/mesolitica/crawl-my-website/resolve/main/melayu-pdf.jsonl
3. Epenerbitan, https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/e-penerbitan.jsonl
4. gov.my pdf, https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/gov.my.jsonl
5. JurnalDBP, https://github.com/mesolitica/malaysian-dataset/tree/master/crawl/jurnaldbp
6. lom.agc.gov.my.jsonl, https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/lom.agc.gov.my.jsonl
7. MS Wikipedia, https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/wikipedia-2023-10-01.jsonl
8. Hansard, https://huggingface.co/datasets/malaysia-ai/dedup-text-dataset/resolve/main/hansard.jsonl

Example of data,

```json
[{'role': 'context',
  'content': 'LIGA\xa0Malaysia (Liga-M) terus menerima tamparan hebat apabila UiTM FC sah menarik diri daripada saingan Liga Super musim ini bagi menyusuli jejak Petaling Jaya City.\n\n\n\r\nPerkara itu disahkan sendiri oleh Presiden The Lion Troops, Profesor Dr. Sazili Shahibi, selepas dua musim beraksi di pentas Liga Super.\n\n\n\r\nSelain masalah kewangan, Dr Sazili menjelaskan ada punca lain mengapa pihak pengurusan mengibarkan bendera putih.\n\n\n \n \n\r\n"Ahli Lembaga Pengarah UiTM telah bermesyuarat dan (kami mengambil) keputusan untuk menarik diri daripada liga pada musim depan.\n\n\n\r\n"Kewangan adalah salah faktornya, tapi kami rasa daripada segi kemampuan, ia tidak sesuai buat pemain-pemain kami," katanya ketika dihubungi \nAstro Arena\n\xa0pada Rabu.\n\n\n\r\nSazili juga berhasrat memaklumkan UiTM bakal beralih ke saingan Liga M3 musim ini.\n\n\n\r\nUntuk rekod, UiTM muncul pasukan berstatus universiti pertama yang layak beraksi dalam Liga Super.\n\n\n\r\nDalam pada itu, Liga Bolasepak Malaysia (MFLhanya akan menjelaskan situasi berkenaan menerusi kenyataan rasmi bakal dalam masa terdekat selepas hanya 14 pasukan yang akan bertanding di pentas Liga Super musim ini. -\nStadium Astro',
  'content_ms': None,
  'indon': False},
 {'role': 'user',
  'content': 'What are the reasons given by UiTM FC for withdrawing from Liga Malaysia?',
  'content_ms': 'Apakah alasan yang diberikan oleh UiTM FC kerana menarik diri daripada Liga Malaysia?',
  'indon': False},
 {'role': 'assistant',
  'content': 'Menurut Presiden UiTM FC, Profesor Dr. Sazili Shahibi, mereka mengambil keputusan untuk menarik diri daripada Liga Malaysia musim ini atas beberapa sebab. Salah satu sebab utamanya adalah masalah kewangan yang dihadapi oleh pasukan. Selain itu, beliau juga menyebut bahawa kemampuan pasukan UiTM tidak sesuai untuk bersaing dalam Liga Super. Selain masalah ini, tidak ada sebab lain yang diberikan dalam laporan tersebut.',
  'content_ms': 'Menurut Presiden UiTM FC, Profesor Dr. Sazili Shahibi, mereka membuat keputusan untuk menarik diri daripada Liga Malaysia musim ini atas beberapa sebab. Salah satu sebab utama ialah masalah kewangan yang dihadapi oleh pasukan. Selain itu, beliau juga menyatakan bahawa keupayaan pasukan UiTM tidak sesuai untuk bersaing dalam Liga Super. Selain masalah ini, tiada sebab lain diberikan dalam laporan tersebut.',
  'indon': False},
 {'role': 'user',
  'content': 'Alamak, memang sedihlah tengok UiTM FC tarik diri dari Liga Malaysia. Macam mana pula dengan penonton setia yang selalu sokong pasukan tu? Harap-harap ada jalan penyelesaian untuk masalah kewangan mereka.',
  'content_ms': 'Alamak, memang sedih tengok UiTM FC menarik diri dari Liga Malaysia. Bagaimana pula dengan penonton setia yang selalu menyokong pasukan itu? Harap-harap ada jalan penyelesaian untuk masalah kewangan mereka.',
  'indon': False},
 {'role': 'assistant',
  'content': 'Ya, memang sedih melihat UiTM FC menarik diri dari Liga Malaysia. Bagi penonton setia yang sentiasa menyokong pasukan tersebut, tentu mereka juga berasa kecewa. Kami juga berharap ada jalan penyelesaian untuk masalah kewangan yang dihadapi oleh UiTM FC. Mungkin pihak pengurusan boleh mencari sponsor atau menyusun semula strategi kewangan untuk membolehkan pasukan tersebut terus beraksi dalam liga pada masa hadapan. Semoga mereka dapat menemui penyelesaian yang baik dan kembali bersaing di pentas bola sepak Malaysia.',
  'content_ms': 'Ya, memang sedih melihat UiTM FC menarik diri dari Liga Malaysia. Bagi penonton setia yang sentiasa menyokong pasukan tersebut, tentu mereka juga berasa kecewa. Kami juga berharap ada jalan penyelesaian untuk masalah kewangan yang dihadapi oleh UiTM FC. Mungkin pihak pengurusan boleh mencari penaja atau menyusun semula strategi kewangan untuk membolehkan pasukan tersebut terus beraksi dalam liga pada masa hadapan. Semoga mereka dapat menemui penyelesaian yang baik dan kembali bersaing di pentas bola sepak Malaysia.',
  'indon': False},
 {'role': 'user',
  'content': 'Ya betul tu, banyak peminat setia UiTM FC yang akan kecewa dengan keputusan mereka tarik diri dari Liga Malaysia. Harapnya pihak pengurusan dapat cari jalan penyelesaian secepat mungkin supaya pasukan tu masih dapat beraksi dalam liga. Saya pun tak sabar nak tengok prestasi UiTM FC lagi musim hadapan. Semoga ada berita baik dalam masa terdekat.',
  'content_ms': 'Ya, betul tu. Banyak peminat setia UiTM FC yang akan kecewa dengan keputusan mereka menarik diri dari Liga Malaysia. Harapnya pihak pengurusan dapat mencari jalan penyelesaian secepat mungkin supaya pasukan itu masih dapat beraksi dalam liga. Saya pun tak sabar nak tengok prestasi UiTM FC lagi musim depan. Semoga ada berita baik dalam masa terdekat.',
  'indon': False},
 {'role': 'assistant',
  'content': 'Saya juga setuju dengan anda. Semoga pihak pengurusan UiTM FC dapat mencari jalan penyelesaian secepat mungkin agar pasukan tersebut masih dapat berlaga dalam Liga Malaysia. Benar, banyak peminat yang ingin melihat prestasi UiTM FC musim hadapan. Mari kita nantikan berita baik daripada mereka dalam masa terdekat. Harapnya mereka dapat mengatasi masalah kewangan dan kembali membanggakan para penyokong. Kita terus sokong UiTM FC!',
  'content_ms': 'Saya juga bersetuju dengan anda. Semoga pihak pengurusan UiTM FC dapat mencari jalan penyelesaian secepat mungkin supaya pasukan tersebut masih dapat bersaing dalam Liga Malaysia. Benar, ramai peminat yang ingin melihat prestasi UiTM FC musim depan. Mari kita nantikan berita baik daripada mereka dalam masa terdekat. Harapnya mereka dapat mengatasi masalah kewangan dan kembali membanggakan para penyokong. Kita terus sokong UiTM FC!',
  'indon': False},
 {'role': 'user',
  'content': 'Ya lah, harapnya UiTM FC dapat dapat mencari penyelesaian yang cepat. Penyokong setia UiTM FC mesti excited nak tengok pasukan beraksi lagi musim hadapan. Semoga ada berita gembira dalam masa terdekat!',
  'content_ms': 'Ya lah, harapnya UiTM FC dapat mencari penyelesaian yang cepat. Penyokong setia UiTM FC mesti teruja untuk melihat pasukan beraksi lagi musim depan. Semoga ada berita gembira dalam masa terdekat!',
  'indon': False},
 {'role': 'assistant',
  'content': 'Betul tu, penyokong setia UiTM FC pasti sangat teruja melihat pasukan beraksi di musim hadapan. Kita harap pihak pengurusan dapat mencari penyelesaian dengan pantas supaya pasukan dapat kembali ke gelanggang. Kita tunggu berita gembira yang akan datang dan terus menyokong UiTM FC dengan penuh semangat. Biar bola sepak Malaysia sentiasa berwarna dengan kehadiran pasukan hebat seperti UiTM FC!',
  'content_ms': 'Betul tu, penyokong setia UiTM FC pasti sangat teruja melihat pasukan beraksi pada musim depan. Kita harap pihak pengurusan dapat mencari penyelesaian dengan pantas supaya pasukan dapat kembali ke gelanggang. Kita tunggu berita gembira yang akan datang dan terus menyokong UiTM FC dengan penuh semangat. Biar bola sepak Malaysia sentiasa berwarna dengan kehadiran pasukan hebat seperti UiTM FC!',
  'indon': False},
 {'role': 'user',
  'content': 'Ya betul tu, memang berharap pasukan UiTM FC dapat segera mencari jalan penyelesaian. Setiap pasukan memang perlu sokongan dan kami sebagai penyokong setia akan terus memberikan sokongan kepada pasukan kesayangan kami. Semoga ada berita gembira yang akan datang!',
  'content_ms': 'Ya, betul tu. Memang berharap pasukan UiTM FC dapat segera mencari jalan penyelesaian. Setiap pasukan memang perlukan sokongan dan kami sebagai penyokong setia akan terus memberikan sokongan kepada pasukan kesayangan kami. Semoga ada berita gembira yang akan datang!',
  'indon': False},
 {'role': 'assistant',
  'content': 'Setiap pasukan memang memerlukan sokongan daripada penyokong setia seperti anda. Anda adalah aset berharga bagi pasukan UiTM FC. Teruskan menyokong dengan penuh semangat dan harapan. Kita berdoa agar pihak pengurusan dapat mencari jalan penyelesaian dengan segera. Bersama-sama, mari kita nantikan berita gembira yang akan datang dan terus memberikan sokongan kepada pasukan kesayangan kita. UiTM FC pasti akan bangkit dan menyampaikan prestasi yang cemerlang musim hadapan!',
  'content_ms': 'Setiap pasukan memang memerlukan sokongan daripada penyokong setia seperti anda. Anda adalah aset berharga bagi pasukan UiTM FC. Teruskan menyokong dengan penuh semangat dan harapan. Kita berdoa agar pihak pengurusan dapat mencari jalan penyelesaian dengan segera. Bersama-sama, mari kita nantikan berita gembira yang akan datang dan terus memberikan sokongan kepada pasukan kesayangan kita. UiTM FC pasti akan bangkit dan menyampaikan prestasi yang cemerlang musim depan!',
  'indon': False}]
```