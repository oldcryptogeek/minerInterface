import PySimpleGUI as sg
import screeninfo

monitor = [screen for screen in screeninfo.get_monitors() if screen.is_primary][0]

icon_of_window = b'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'

layout = [
    [sg.Text("", key="status", size=(9, 1)),
     sg.ProgressBar(1000, key="progress", size=(round(monitor.width/20.87), 20), orientation='h'),
     sg.Text("", key="progress_percent", size=(9, 1))],

    [sg.Text("", size=(100, 1))],

    [sg.Text('Network IP:', size=(9, 1)),
     sg.InputText(key='miner_network', do_not_clear=True, size=(123, 1)),
     sg.Button('Scan', key='scan')],

    [sg.Text('IP List File:', size=(9, 1)),
     sg.Input(key="file_iplist", do_not_clear=True, size=(123, 1)),
     sg.FileBrowse(),
     sg.Button('Import', key="import_iplist"),
     sg.Button('Export', key="export_iplist")],

    [sg.Text('Config File:', size=(9, 1)),
     sg.Input(key="file_config", do_not_clear=True, size=(123, 1)),
     sg.FileBrowse(),
     sg.Button('Import', key="import_file_config"),
     sg.Button('Export', key="export_file_config")],

    [sg.Column([

        [sg.Column([

            [sg.Text("IP List:", pad=(0, 0)),
             sg.Text("", key="ip_count", pad=(0, 0), size=(3, 1)),
             sg.Button('ALL', key="select_all_ips"),
             sg.Button("REFRESH DATA", key='refresh_data'),
             sg.Button("OPEN IN WEB", key='open_in_web'),
             sg.Button("REBOOT", key='reboot_miners'),
             sg.Button("RESTART BACKEND", key='restart_miner_backend')],

            [sg.Text("HR Total: ", pad=(0, 0)), sg.Text("", key="hr_total")],
        ])],

        [sg.Table(
            values=[],
            headings=["IP", "Model", "Hostname", "Hashrate", "Temperature", "Current User", "Wattage"],
            auto_size_columns=False,
            max_col_width=15,
            justification="center",
            key="ip_table",
            col_widths=[12, 10, 12, 12, 10, 22, 7],
            background_color="white",
            text_color="black",
            size=(115, 27),
            expand_x=True,
            enable_click_events=True,
        )]
    ]),

        sg.Column([
            [sg.Text("Config"), sg.Button("IMPORT", key="import_config"),
             sg.Button("CONFIG", key="send_config"),
             sg.Button("LIGHT", key="light"),
             sg.Button("GENERATE", key="generate_config")],

            [sg.Text("")],

            [sg.Multiline(size=(50, 28), key="config", do_not_clear=True)],

        ])
    ],
]


def generate_config_layout():
    config_layout = [
        [sg.Text("Enter your pool username and password below to generate a config for SlushPool.")],

        [sg.Text("")],

        [sg.Text('Username:', size=(19, 1)),
         sg.InputText(key='generate_config_window_username', do_not_clear=True, size=(45, 1))],

        [sg.Text('Worker Name (OPT):', size=(19, 1)),
         sg.InputText(key='generate_config_window_workername', do_not_clear=True, size=(45, 1))],

        [sg.Text('Allow Stratum V2?:', size=(19, 1)),
         sg.Checkbox('', key='generate_config_window_allow_v2', default=True)],

        [sg.Button("Generate", key="generate_config_window_generate")]
    ]
    return config_layout


window = sg.Window('Upstream Config Util', layout, icon=icon_of_window)
