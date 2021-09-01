# """🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
#                                                              GNU GENERAL PUBLIC LICENSE 
#                                                                Version 3, 29 June 2007
#                                                         Copyright (C) 2007 Free Software Foundation
#                                                 Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
#                                                     of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
#                                                                     •🔺ʏօʊȶʊɮɛʟɨ🔻• 
#                                                     has been licensed under GNU General Public License
#                                                 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
# 🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺"""
FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN apt update && apt upgrade -y && apt install git -y && apt install python3 -y && apt install python3-pip -y && apt install -y ffmpeg opus-tools bpm-tools
RUN git clone https://github.com/HypeVoidSoul/YouTube-Downloader.git
RUN cd YouTube-Downloader
WORKDIR /YouTube-Downloader
RUN pip install -r YouTube.txt
CMD python3 -m •🔺ʏօʊȶʊɮɛʟɨ🔻•
# """🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
#                                                              GNU GENERAL PUBLIC LICENSE 
#                                                                Version 3, 29 June 2007
#                                                         Copyright (C) 2007 Free Software Foundation
#                                                 Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
#                                                     of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
#                                                                     •🔺ʏօʊȶʊɮɛʟɨ🔻• 
#                                                     has been licensed under GNU General Public License
#                                                 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
# 🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺"""