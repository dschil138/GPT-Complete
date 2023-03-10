import rumps
import pynput
from config import *
from functions import *
import api_key 

class MyApp(rumps.App):
    def __init__(self):
        super(MyApp, self).__init__("⚡️")
        self.combination1 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.shift, pynput.keyboard.KeyCode.from_char('k')]
        self.tokens = 250
        self.model = model1
        self.current = set()
        self.listener = None

        self.hotkey_menu = rumps.MenuItem('Hotkey')
        self.cmd_shift_k_menu_item = rumps.MenuItem('Cmd-Shift-k', callback=self.use_cmd_shift_k_hotkey)
        self.ctrl_zero_menu_item = rumps.MenuItem('Ctrl-0', callback=self.use_ctrl_zero_hotkey)
        self.cmd_enter_menu_item = rumps.MenuItem('Cmd-Enter', callback=self.use_cmd_enter_hotkey)
        self.rightctrl_leftalt_menu_item = rumps.MenuItem('Right-Ctrl + Left-Alt', callback=self.use_rightctrl_leftalt_hotkey)
        self.hotkey_menu.add(self.cmd_shift_k_menu_item)
        self.hotkey_menu.add(self.ctrl_zero_menu_item)
        self.hotkey_menu.add(self.cmd_enter_menu_item)
        self.hotkey_menu.add(self.rightctrl_leftalt_menu_item)
        self.cmd_shift_k_menu_item.state = True

        self.model_menu = rumps.MenuItem('Model')
        self.ada_menu_item = rumps.MenuItem('text-ada-001', callback=self.use_ada)
        self.babbage_menu_item = rumps.MenuItem('text-babbage-001', callback=self.use_babbage)
        self.curie_menu_item = rumps.MenuItem('text-curie-001', callback=self.use_curie)
        self.davinci_menu_item = rumps.MenuItem('text-davinci-003', callback=self.use_davinci)
        self.codex_menu_item = rumps.MenuItem('code-davinci-002', callback=self.use_codex)
        self.model_menu.add(self.ada_menu_item)
        self.model_menu.add(self.babbage_menu_item)
        self.model_menu.add(self.curie_menu_item)
        self.model_menu.add(self.davinci_menu_item)
        self.model_menu.add(self.codex_menu_item)
        self.davinci_menu_item.state = True

        self.tokens_menu = rumps.MenuItem('Max Tokens')
        self.tokens_100_menu_item = rumps.MenuItem(100, callback=self.use_100_tokens)
        self.tokens_250_menu_item = rumps.MenuItem(250, callback=self.use_250_tokens)
        self.tokens_500_menu_item = rumps.MenuItem(500, callback=self.use_500_tokens)
        self.tokens_800_menu_item = rumps.MenuItem(800, callback=self.use_800_tokens)
        self.tokens_menu.add(self.tokens_100_menu_item)
        self.tokens_menu.add(self.tokens_250_menu_item)
        self.tokens_menu.add(self.tokens_500_menu_item)
        self.tokens_menu.add(self.tokens_800_menu_item)
        self.tokens_250_menu_item.state = True

        self.menu.add(self.hotkey_menu)
        self.menu.add(self.model_menu)
        self.menu.add(self.tokens_menu)
        
    def use_cmd_shift_k_hotkey(self, sender):
        self.combination1 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.shift, pynput.keyboard.KeyCode.from_char('k')]
        self.cmd_shift_k_menu_item.state, self.ctrl_zero_menu_item.state, self.cmd_enter_menu_item.state, self.rightctrl_leftalt_menu_item.state = True, False, False, False
    def use_ctrl_zero_hotkey(self, sender):
        self.combination1 = [pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('0')]
        self.cmd_shift_k_menu_item.state, self.ctrl_zero_menu_item.state, self.cmd_enter_menu_item.state, self.rightctrl_leftalt_menu_item.state = False, True, False, False
    def use_cmd_enter_hotkey(self, sender):
        self.combination1 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.enter]
        self.cmd_shift_k_menu_item.state, self.ctrl_zero_menu_item.state, self.cmd_enter_menu_item.state, self.rightctrl_leftalt_menu_item.state = False, False, True, False
    def use_rightctrl_leftalt_hotkey(self, sender):
        self.combination1 = [pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.alt_l]
        self.cmd_shift_k_menu_item.state, self.ctrl_zero_menu_item.state, self.cmd_enter_menu_item.state, self.rightctrl_leftalt_menu_item.state = False, False, False, True

    def use_ada(self, sender):
        self.model1 = "text-ada-001"
        self.ada_menu_item.state, self.babbage_menu_item.state, self.curie_menu_item.state, self.davinci_menu_item.state, self.codex_menu_item.state = True, False, False, False, False
    def use_babbage(self, sender):
        self.model1 = "text-babbage-001"
        self.ada_menu_item.state, self.babbage_menu_item.state, self.curie_menu_item.state, self.davinci_menu_item.state, self.codex_menu_item.state = False, True, False, False, False
    def use_curie(self, sender):
        self.model1 = "text-curie-001"
        self.ada_menu_item.state, self.babbage_menu_item.state, self.curie_menu_item.state, self.davinci_menu_item.state, self.codex_menu_item.state = False, False, True, False, False
    def use_davinci(self, sender):
        self.model1 = "text-davinci-003"
        self.ada_menu_item.state, self.babbage_menu_item.state, self.curie_menu_item.state, self.davinci_menu_item.state, self.codex_menu_item.state = False, False, False, True, False
    def use_codex(self, sender):
        self.model1 = "code-davinci-002"
        self.ada_menu_item.state, self.babbage_menu_item.state, self.curie_menu_item.state, self.davinci_menu_item.state, self.codex_menu_item.state = False, False, False, False, True

    def use_100_tokens(self, sender):
        self.tokens = "100"
        self.tokens_100_menu_item.state, self.tokens_250_menu_item.state, self.tokens_500_menu_item.state, self.tokens_800_menu_item.state = True, False, False, False
    def use_250_tokens(self, sender):
        self.tokens = "250"
        self.tokens_100_menu_item.state, self.tokens_250_menu_item.state, self.tokens_500_menu_item.state, self.tokens_800_menu_item.state = False, True, False, False
    def use_500_tokens(self, sender):
        self.tokens = "500"
        self.tokens_100_menu_item.state, self.tokens_250_menu_item.state, self.tokens_500_menu_item.state, self.tokens_800_menu_item.state = False, False, True, False
    def use_800_tokens(self, sender):
        self.tokens = "800"
        self.tokens_100_menu_item.state, self.tokens_250_menu_item.state, self.tokens_500_menu_item.state, self.tokens_800_menu_item.state = False, False, False, True


    def main_function(self, model_var, tokens_var):
        print(model1)
        self.current.clear()
        user_input = check_and_select_input()
        print('sending to API')
        botResponse = send_to_bot(universal_prepend, model_var, user_input, tokens_var)
        paste_response(botResponse)

    def on_press(self, key):
        self.current.add(key)
        if all(k in self.current for k in self.combination1):
            int_tokens = int(self.tokens)
            self.main_function(self.model1, int_tokens)

    def on_release(self, key):
        if key in self.current:
            self.current.remove(key)

    def start_listener(self):
        self.listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            self.listener = None

    def quit_application(self, *args, **kwargs):
        self.stop_listener()
        super(MyApp, self).quit_application(*args, **kwargs)


if __name__ == '__main__':
    myApp = MyApp()
    myApp.start_listener()
    myApp.run()
