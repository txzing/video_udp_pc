set_property SRC_FILE_INFO {cfile:d:/workdir/pic_lwip_udp/video_mix/vivado/vivado_proj/vivado_proj.srcs/sources_1/bd/system/ip/system_zynq_ultra_ps_e_0_0/system_zynq_ultra_ps_e_0_0/system_zynq_ultra_ps_e_0_0_in_context.xdc rfile:../../../vivado_proj.srcs/sources_1/bd/system/ip/system_zynq_ultra_ps_e_0_0/system_zynq_ultra_ps_e_0_0/system_zynq_ultra_ps_e_0_0_in_context.xdc id:1 order:EARLY scoped_inst:system_i/processer_ss/zynq_ultra_ps_e_0} [current_design]
set_property SRC_FILE_INFO {cfile:d:/workdir/pic_lwip_udp/video_mix/vivado/vivado_proj/vivado_proj.srcs/sources_1/bd/system/ip/system_clk_wiz_0_0/system_clk_wiz_0_0/system_clk_wiz_0_0_in_context.xdc rfile:../../../vivado_proj.srcs/sources_1/bd/system/ip/system_clk_wiz_0_0/system_clk_wiz_0_0/system_clk_wiz_0_0_in_context.xdc id:2 order:EARLY scoped_inst:system_i/vid_out_ss/clk_wiz_0} [current_design]
set_property SRC_FILE_INFO {cfile:D:/workdir/pic_lwip_udp/video_mix/vivado/vivado_proj/vivado_proj.srcs/constrs_1/imports/xdc/system.xdc rfile:../../../vivado_proj.srcs/constrs_1/imports/xdc/system.xdc id:3} [current_design]
current_instance system_i/processer_ss/zynq_ultra_ps_e_0
set_property src_info {type:SCOPED_XDC file:1 line:2 export:INPUT save:INPUT read:READ} [current_design]
create_clock -period 5.000 [get_ports {}]
set_property src_info {type:SCOPED_XDC file:1 line:4 export:INPUT save:INPUT read:READ} [current_design]
create_clock -period 3.333 [get_ports {}]
current_instance
current_instance system_i/vid_out_ss/clk_wiz_0
set_property src_info {type:SCOPED_XDC file:2 line:1 export:INPUT save:INPUT read:READ} [current_design]
create_clock -period 5.000 [get_ports -no_traverse {}]
set_property src_info {type:SCOPED_XDC file:2 line:4 export:INPUT save:INPUT read:READ} [current_design]
create_generated_clock -source [get_ports clk_in1] -edges {1 2 3} -edge_shift {0.000 0.867 1.734} [get_ports {}]
set_property src_info {type:SCOPED_XDC file:2 line:6 export:INPUT save:INPUT read:READ} [current_design]
create_generated_clock -source [get_ports clk_in1] -edges {1 2 3} -edge_shift {0.000 14.076 28.152} [get_ports {}]
set_property src_info {type:SCOPED_XDC file:2 line:8 export:INPUT save:INPUT read:READ} [current_design]
create_generated_clock -source [get_ports clk_in1] -edges {1 2 3} -edge_shift {0.000 14.076 28.152} [get_ports {}]
current_instance
set_property src_info {type:XDC file:3 line:3 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AG13 [get_ports uart_0_rxd]
set_property src_info {type:XDC file:3 line:5 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN W11 [get_ports uart_0_txd]
set_property src_info {type:XDC file:3 line:10 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AA12 [get_ports sil9136_sda_io]
set_property src_info {type:XDC file:3 line:13 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN Y12 [get_ports sil9136_scl_io]
set_property src_info {type:XDC file:3 line:18 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AC13 [get_ports vid_clk]
set_property src_info {type:XDC file:3 line:21 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN Y14 [get_ports vid_de]
set_property src_info {type:XDC file:3 line:24 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AC14 [get_ports vid_vs]
set_property src_info {type:XDC file:3 line:27 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN Y13 [get_ports vid_hs]
set_property src_info {type:XDC file:3 line:31 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN L13 [get_ports {vid_data[0]}]
set_property src_info {type:XDC file:3 line:32 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN L14 [get_ports {vid_data[1]}]
set_property src_info {type:XDC file:3 line:33 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN C14 [get_ports {vid_data[2]}]
set_property src_info {type:XDC file:3 line:34 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN C13 [get_ports {vid_data[3]}]
set_property src_info {type:XDC file:3 line:35 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN B14 [get_ports {vid_data[4]}]
set_property src_info {type:XDC file:3 line:36 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN A14 [get_ports {vid_data[5]}]
set_property src_info {type:XDC file:3 line:37 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN B13 [get_ports {vid_data[6]}]
set_property src_info {type:XDC file:3 line:38 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN A13 [get_ports {vid_data[7]}]
set_property src_info {type:XDC file:3 line:39 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN K14 [get_ports {vid_data[8]}]
set_property src_info {type:XDC file:3 line:40 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN J14 [get_ports {vid_data[9]}]
set_property src_info {type:XDC file:3 line:41 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN H13 [get_ports {vid_data[10]}]
set_property src_info {type:XDC file:3 line:42 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN H14 [get_ports {vid_data[11]}]
set_property src_info {type:XDC file:3 line:43 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN F13 [get_ports {vid_data[12]}]
set_property src_info {type:XDC file:3 line:44 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN G13 [get_ports {vid_data[13]}]
set_property src_info {type:XDC file:3 line:45 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN G14 [get_ports {vid_data[14]}]
set_property src_info {type:XDC file:3 line:46 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN G15 [get_ports {vid_data[15]}]
set_property src_info {type:XDC file:3 line:47 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN A11 [get_ports {vid_data[16]}]
set_property src_info {type:XDC file:3 line:48 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN A12 [get_ports {vid_data[17]}]
set_property src_info {type:XDC file:3 line:49 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN C12 [get_ports {vid_data[18]}]
set_property src_info {type:XDC file:3 line:50 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN D12 [get_ports {vid_data[19]}]
set_property src_info {type:XDC file:3 line:51 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN A10 [get_ports {vid_data[20]}]
set_property src_info {type:XDC file:3 line:52 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN B11 [get_ports {vid_data[21]}]
set_property src_info {type:XDC file:3 line:53 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN B10 [get_ports {vid_data[22]}]
set_property src_info {type:XDC file:3 line:54 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN C11 [get_ports {vid_data[23]}]
set_property src_info {type:XDC file:3 line:61 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AB14 [get_ports eeprom_wp]
set_property src_info {type:XDC file:3 line:64 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN W14 [get_ports eeprom_sda_io]
set_property src_info {type:XDC file:3 line:67 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AB15 [get_ports eeprom_scl_io]
set_property src_info {type:XDC file:3 line:72 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AG11 [get_ports {gpio_tri_io[0]}]
set_property src_info {type:XDC file:3 line:76 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AE15 [get_ports {gpio_tri_io[1]}]
set_property src_info {type:XDC file:3 line:80 export:INPUT save:INPUT read:READ} [current_design]
set_property PACKAGE_PIN AH13 [get_ports {gpio_tri_io[2]}]