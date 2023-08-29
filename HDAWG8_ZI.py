class AWG_ZI:
    def __init__(self, hdawg, grouping=2, seq_pgm=None, awg_name=None, readout=None, qubit=None, coupler=None):
        self.hdawg = hdawg
        self.grouping = grouping
        self.seq_pgm = seq_pgm
        print('Initialized')
        
        self.ro = readout
        self.q = qubit
        self.cpl = coupler
        
        if readout is not None:
            self.awg_name_init = self.ro.awg_name
            self.awg_name_ro = self.ro.awg_name
            self.awg_name = self.ro.awg_name
        if qubit is not None:
            self.awg_name_init = self.q.awg_name_IQ
            self.awg_name_IQ = self.q.awg_name_IQ
            self.awg_name_flux_DC = self.q.awg_name_flux_DC
            self.awg_name_flux_RF = self.q.awg_name_flux_RF
        if coupler is not None:
            self.awg_name_cpl = self.cpl.awg_name
            
        self.hdawgModule = hdawg.awgModule()
        self.hdawgModule.execute()
        self.hdawgModule.set('awgModule/device', self.awg_name_init)
        self.hdawgModule.set('awgModule/index', 0)
        self.hdawgModule.set('awgModule/awg/enable', 0)
                        
    # QUBIT
    # ON/OFF methods
    def disable_qubit_IQ_output(self):
        """
        Выключает IQ-каналы RF-сигналов кубита
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_I}/on',0)
        self.hdawg.setInt(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_Q}/on',0)
           
    def enable_qubit_IQ_output(self):
        """
        Включает IQ-каналы RF-сигналов кубита
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_I}/on',1)
        self.hdawg.setInt(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_Q}/on',1)

    def disable_qubit_flux_RF(self):
        """
        Выключает RF-канал флакса кубита
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_flux_RF}/sigouts/{self.q.ch_flux_RF}/on',0)
           
    def enable_qubit_flux_RF(self):
        """
        Включает RF-канал флакса кубита
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_flux_RF}/sigouts/{self.q.ch_flux_RF}/on',1)
        
    def disable_qubit_flux_DC(self):
        """
        Выключает DC-канал флакса кубита
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_flux_DC}/sigouts/{self.q.ch_flux_DC}/on',0)
           
    def enable_qubit_flux_DC(self):
        """
        Включает DC-канал флакса кубита
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_flux_DC}/sigouts/{self.q.ch_flux_DC}/on',1)
        
    def disable_sequencer(self):
        """
        +checked
        """
        self.hdawg.setInt(f"/{self.q.awg_name_IQ}/awgs/{self.q.seq_num}/enable", 0)
    
    def enable_sequencer(self):
        """
        +checked
        """
        self.hdawg.setInt(f"/{self.q.awg_name_IQ}/awgs/{self.q.seq_num}/enable", 1)
        
               
    # SET/GET methods
    def set_qubit_IQ_range(self):
        """
        Выставляет диапазоны по напряжению на IQ-каналы RF-сигналов кубита
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_I}/range', self.q.range_IQ)
        self.hdawg.setDouble(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_Q}/range', self.q.range_IQ)
        
    def set_qubit_flux_RF_range(self):
        """
        Выставляет диапазон по напряжению на RF-канал флакса кубита
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_flux_RF}/sigouts/{self.q.ch_flux_RF}/range', self.q.range_flux_RF)
        
    def set_qubit_IQ_offset(self):
        """
        Выставляет оффсеты (смещения) по напряжению на IQ-каналы RF-сигналов кубита
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_I}/offset', np.real(self.q.dc_q))
        self.hdawg.setDouble(f'/{self.awg_name_IQ}/sigouts/{self.q.ch_Q}/offset', np.imag(self.q.dc_q))
        
    def set_qubit_flux_RF_offset(self):
        """
        Выставляет оффсет (смещение) по напряжению на RF-канал флакса кубита
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_flux_RF}/sigouts/{self.q.ch_flux_RF}/offset', self.q.flux_RF_offset)
        
    def set_qubit_flux_DC_offset(self):
        """
        Выставляет оффсет (смещение) по напряжению на DC-канал флакса кубита
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_flux_DC}/sigouts/{self.q.ch_flux_DC}/offset', self.q.flux_DC_offset)

    # READOUT
    # ON/OFF methods
    def disable_readout_IQ_output(self):
        """
        Выключает IQ-каналы RF-сигналов считывания
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_I}/on',0)
        self.hdawg.setInt(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_Q}/on',0)
           
    def enable_readout_IQ_output(self):
        """
        Включает IQ-каналы RF-сигналов считывания
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_I}/on',1)
        self.hdawg.setInt(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_Q}/on',1)
        
    # SET/GET methods
    def set_readout_IQ_range(self):
        """
        Выставляет диапазоны по напряжению на IQ-каналы RF-сигналов считывания
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_I}/range', self.ro.range_IQ)
        self.hdawg.setDouble(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_Q}/range', self.ro.range_IQ)
    
    def set_readout_IQ_offset(self):
        """
        Выставляет оффсеты (смещения) по напряжению на IQ-каналы RF-сигналов считывания
        +checked
        """
        self.hdawg.setDouble(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_I}/offset', np.real(self.ro.dc_res))
        self.hdawg.setDouble(f'/{self.awg_name_ro}/sigouts/{self.ro.ch_Q}/offset', np.imag(self.ro.dc_res))
        
    def configure_readout_triggers(self):
        """
        +checked
        """
        self.hdawg.setInt(f'/{self.awg_name_ro}/awgs/{self.ro.awg_num}/auxtriggers/0/slope', 2)
        self.hdawg.setInt(f'/{self.awg_name_ro}/triggers/out/1/source', 1)
        self.hdawg.setInt(f'/{self.awg_name_ro}/triggers/streams/0/enable', 1)
        self.hdawg.setInt(f'/{self.awg_name_ro}/triggers/streams/0/mask', 0x001)
        
        
    # COUPLER 
    # ON/OFF methods
    def disable_coupler_output(self):
        """
        """
        self.hdawg.setInt(f'/{self.awg_name_cpl}/sigouts/{self.cpl.ch_cpl}/on',0)
           
    def enable_coupler_output(self):
        """
        """
        self.hdawg.setInt(f'/{self.awg_name_cpl}/sigouts/{self.cpl.ch_cpl}/on',1)
            
    # SET/GET methods
    def set_coupler_DC_offset(self):
        """
        """
        self.hdawg.setDouble(f'/{self.awg_name_cpl}/sigouts/{self.q.ch_flux_DC}/offset', self.q.flux_DC_offset)
        
        
    def disable_all_awg_outputs(self):
        """
        """
        for channel in range(7):
            self.hdawg.setInt(f'/{self.hdawg_name}/sigouts/{channel}/on',0)

    
    def set_channels_grouping(self):
        self.hdawg.setInt(f'/{self.awg_name}/system/awg/channelgrouping', self.grouping)