# ComputerAccessWithOneKey_SettingGUI
Python version: 3.8.10
<br>
.exe 파일 생성)<br>>pyinstaller -w -F --icon=setting.ico setting_ui_modified.py
<br><br>
설정 파일입니다.<br>
setting_ui_modified.py 만 유효한 코드입니다.<br>
기타 파일은 이후 삭제할 예정입니다.
<br><br>
setting_ui_modified.py 파일의 대부분은 .ui파일을 .py 파일로 변환시키면서 자동 생성된 코드이고, 일부 수정을 진행했습니다.<br>
추가로 작성한 부분은 2280번째 줄의 self.return_default(),<br>
2444줄부터 버튼에 할당하는 함수 입니다.<br>
기타 수정사항은 .ui파일을 .py 파일로 변환시키고 오류가 난다면 해당 부분을 확인해주세요.
<br><br>
setting.ui 파일은 qtdesigner에서 작업할 수 있습니다.
<br>
프로그램을 통하지 않고 값을 수정하려면, <a href="https://handh0.tistory.com/4">이 내용</a>을 참고해서 직접 수정할 수 있습니다.
