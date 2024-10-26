from xdevice.__main__ import main_process

if __name__ == "__main__":
  # 应用启动测试。
  # main_process("run -l AbilityTest -ta agent_mode:bin;screenshot:true")

  # 首页 - 头条测试。
  # main_process("run -l NewsTest -ta agent_mode:bin;screenshot:true")

  # 首页 - 菜谱测试。
  main_process("run -l MenuTest -ta agent_mode:bin;screenshot:true")