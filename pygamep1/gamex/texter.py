from ursina import *
app = Ursina()
descr = dedent('''
      <scale:1.5><orange>Rainstorm<default><scale:1>
      Summon a <azure>rain storm <default>to deal 5 <azure>water

      damage <default>to <hsb(0,1,.7)>everyone, <default><image:file_icon> <red><image:file_icon> test <default>including <orange>yourself. <default>
      Lasts for 4 rounds.''').strip()

Text.default_resolution = 1080 * Text.size
test = Text(text=descr, origin=(0,0), background=True)




def input(key):
      if key == 'a':
          print('a')
          test.text = '<default><image:file_icon> <red><image:file_icon> test '
          print('by', test.text)

window.fps_counter.enabled = False
print('....', Text.get_width('yolo'))
app.run()