"""将 Xiangqi.com 发布的象棋音效转成单声道 Ogg Vorbis；需 FFmpeg。"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess


SOURCE = Path(__file__).resolve().parent
CARD = SOURCE.parents[1] / 'assets/card'


def merge(path, updates):
    current = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    current.update(updates)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(current, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ffmpeg', default=shutil.which('ffmpeg'))
    args = parser.parse_args()
    if not args.ffmpeg:
        parser.error('需要 FFmpeg，可用 --ffmpeg 指定路径')
    manifest = json.loads((SOURCE/'sounds/source_manifest.json').read_text(encoding='utf-8'))
    output = CARD/'sounds/xiangqi'
    output.mkdir(parents=True, exist_ok=True)
    for record in manifest['sources']:
        source = SOURCE/'sounds'/record['file']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == record['sha256'], source
        name = 'gong' if source.stem == 'gong-game-start-end' else source.stem
        subprocess.run([args.ffmpeg,'-hide_banner','-loglevel','error','-y','-i',str(source),'-map_metadata','-1',
                        '-ac','1','-ar','44100','-fflags','+bitexact','-flags:a','+bitexact','-c:a','libvorbis','-q:a','6',str(output/(name+'.ogg'))], check=True)
    events = {}
    for event, name in [('move','move'),('capture','capture'),('start','gong'),('end','gong')]:
        events['xiangqi.'+event] = {'subtitle':'subtitles.card.xiangqi.'+event,
                                  'sounds':[{'name':'card:xiangqi/'+name,'attenuation_distance':12}]}
    for event, name, pitch in [('check','bell',1.2),('illegal','bass',0.7)]:
        events['xiangqi.'+event] = {'subtitle':'subtitles.card.xiangqi.'+event,
                                  'sounds':[{'name':'minecraft:block.note_block.'+name,'type':'event','pitch':pitch}]}
    merge(CARD/'sounds.json', events)
    names = ['move','capture','check','start','end','illegal']
    for language, text in [('zh_cn',['象棋落子','象棋吃子','将军','象棋开局','象棋结束','走法不合法']),
                           ('en_us',['Xiangqi move','Xiangqi capture','Check','Xiangqi starts','Xiangqi ends','Illegal move'])]:
        merge(CARD/'lang'/(language+'.json'), {'subtitles.card.xiangqi.'+n:t for n,t in zip(names,text)})
    print('Generated Xiangqi.com move/capture/gong and vanilla check/illegal cues.')


if __name__ == '__main__':
    main()
