// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2020.1 (64-bit)
// Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
// ==============================================================
`timescale 1 ns / 1 ps
(* rom_style = "distributed" *) module system_v_tpg_1_1_tpgPatternCrossHaDeQ_rom (
addr0, ce0, q0, clk);

parameter DWIDTH = 8;
parameter AWIDTH = 2;
parameter MEM_SIZE = 3;

input[AWIDTH-1:0] addr0;
input ce0;
output reg[DWIDTH-1:0] q0;
input clk;

(* ram_style = "distributed" *)reg [DWIDTH-1:0] ram[0:MEM_SIZE-1];

initial begin
    $readmemh("./system_v_tpg_1_1_tpgPatternCrossHaDeQ_rom.dat", ram);
end



always @(posedge clk)  
begin 
    if (ce0) 
    begin
        q0 <= ram[addr0];
    end
end



endmodule

`timescale 1 ns / 1 ps
module system_v_tpg_1_1_tpgPatternCrossHaDeQ(
    reset,
    clk,
    address0,
    ce0,
    q0);

parameter DataWidth = 32'd8;
parameter AddressRange = 32'd3;
parameter AddressWidth = 32'd2;
input reset;
input clk;
input[AddressWidth - 1:0] address0;
input ce0;
output[DataWidth - 1:0] q0;



system_v_tpg_1_1_tpgPatternCrossHaDeQ_rom system_v_tpg_1_1_tpgPatternCrossHaDeQ_rom_U(
    .clk( clk ),
    .addr0( address0 ),
    .ce0( ce0 ),
    .q0( q0 ));

endmodule
