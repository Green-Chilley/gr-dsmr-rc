/* -*- c++ -*- */
/*
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_DSMX_DESPREADER_IMPL_H
#define INCLUDED_DSMX_DESPREADER_IMPL_H

#include <stdio.h>
#include <gnuradio/pdu.h>
#include <gnuradio/dsmx/Despreader.h>

namespace gr {
  namespace dsmx {

    class Despreader_impl : public Despreader
    {
     private:
      // Nothing to declare in this block.
      void callback(pmt::pmt_t msg);
      void callback_SDR(pmt::pmt_t msg);
      void callback_8DR(pmt::pmt_t msg);
      void crc_update(uint16_t data, bool reverse);
      void crc_update(uint8_t data, bool reverse);
      void crc_seed_set(uint8_t seed_MSB, uint8_t seed_LSB);
      void crc_seed_set(uint16_t seed);
      int get_next_channel(int current);
      uint16_t crc_calc(uint16_t data[8], uint8_t length, uint16_t seed, bool reverse);
      uint16_t crc_seed_find(uint16_t data[8], uint8_t length, uint16_t transmitted);



      int d_row,d_column;
      int d_channel;
      pmt::pmt_t d_pdu_meta;
      pmt::pmt_t d_pdu_vector;
      gr::types::vector_type d_type;
      uint8_t d_channels[23];
      uint16_t d_data_chunks[4], d_crc_recieved=0;
      uint16_t d_high_reminder, d_reminder;
      uint16_t mfg_id[4];
      uint16_t sum;
      uint16_t rcvdSum;

      uint16_t msbId = 0xC5; // 0xC5 or 0x49
      uint16_t lsbId = 0x9C; // 0x9C or 0xB6
      uint16_t firstId = 0xC59C; // 0xC59C or 0x49B6
      uint16_t secondId = 0x0D76;

      //uint64_t altcode = 0x88E1D631265FBD40;



     public:
      Despreader_impl();
      ~Despreader_impl();


      static uint8_t reverse(uint8_t b);
      static uint16_t reverse_bytes(uint16_t b);
      static uint16_t reverse_bits_in_bytes(uint16_t b);
      static uint16_t reverse_all(uint16_t b);
      static uint16_t switch_to_crc_pn_scheme(uint16_t b);
      void calc_dsmx_channel(uint16_t byte01, uint16_t byte23);
      static uint64_t cast864(uint8_t data[8]);
      static uint64_t cast864reverse(uint8_t data[8]);
      
      static uint32_t cast432(uint8_t data[4]);
      static uint32_t cast432reverse(uint8_t data[4]);
      

      uint16_t update_crc_16( uint16_t crc, unsigned char c , bool reverse);
      void init_crc16_tab( void );
      bool crc_tab16_init;
      uint16_t crc_tab16[256];


      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };
    

      static uint8_t pncodes[5][9][8] = {
      /* Note these are in order transmitted (LSB 1st) */
      { /* Row 0 */
        /* Col 0 */ {0x03, 0xBC, 0x6E, 0x8A, 0xEF, 0xBD, 0xFE, 0xF8},
        /* Col 1 */ {0x88, 0x17, 0x13, 0x3B, 0x2D, 0xBF, 0x06, 0xD6},
        /* Col 2 */ {0xF1, 0x94, 0x30, 0x21, 0xA1, 0x1C, 0x88, 0xA9},
        /* Col 3 */ {0xD0, 0xD2, 0x8E, 0xBC, 0x82, 0x2F, 0xE3, 0xB4},
        /* Col 4 */ {0x8C, 0xFA, 0x47, 0x9B, 0x83, 0xA5, 0x66, 0xD0},
        /* Col 5 */ {0x07, 0xBD, 0x9F, 0x26, 0xC8, 0x31, 0x0F, 0xB8},
        /* Col 6 */ {0xEF, 0x03, 0x95, 0x89, 0xB4, 0x71, 0x61, 0x9D},
        /* Col 7 */ {0x40, 0xBA, 0x97, 0xD5, 0x86, 0x4F, 0xCC, 0xD1},
        /* Col 8 */ {0xD7, 0xA1, 0x54, 0xB1, 0x5E, 0x89, 0xAE, 0x86}
      },
      { /* Row 1 */
        /* Col 0 */ {0x83, 0xF7, 0xA8, 0x2D, 0x7A, 0x44, 0x64, 0xD3},
        /* Col 1 */ {0x3F, 0x2C, 0x4E, 0xAA, 0x71, 0x48, 0x7A, 0xC9},
        /* Col 2 */ {0x17, 0xFF, 0x9E, 0x21, 0x36, 0x90, 0xC7, 0x82},
        /* Col 3 */ {0xBC, 0x5D, 0x9A, 0x5B, 0xEE, 0x7F, 0x42, 0xEB},
        /* Col 4 */ {0x24, 0xF5, 0xDD, 0xF8, 0x7A, 0x77, 0x74, 0xE7},
        /* Col 5 */ {0x3D, 0x70, 0x7C, 0x94, 0xDC, 0x84, 0xAD, 0x95},
        /* Col 6 */ {0x1E, 0x6A, 0xF0, 0x37, 0x52, 0x7B, 0x11, 0xD4},
        /* Col 7 */ {0x62, 0xF5, 0x2B, 0xAA, 0xFC, 0x33, 0xBF, 0xAF},
        /* Col 8 */ {0x40, 0x56, 0x32, 0xD9, 0x0F, 0xD9, 0x5D, 0x97}
                    // {0,0,0,0,0,0,0,0}
      },
      { /* Row 2 */
        /* Col 0 */ {0x40, 0x56, 0x32, 0xD9, 0x0F, 0xD9, 0x5D, 0x97},
        /* Col 1 */ {0x8E, 0x4A, 0xD0, 0xA9, 0xA7, 0xFF, 0x20, 0xCA},
        /* Col 2 */ {0x4C, 0x97, 0x9D, 0xBF, 0xB8, 0x3D, 0xB5, 0xBE},
        /* Col 3 */ {0x0C, 0x5D, 0x24, 0x30, 0x9F, 0xCA, 0x6D, 0xBD},
        /* Col 4 */ {0x50, 0x14, 0x33, 0xDE, 0xF1, 0x78, 0x95, 0xAD},
        /* Col 5 */ {0x0C, 0x3C, 0xFA, 0xF9, 0xF0, 0xF2, 0x10, 0xC9},
        /* Col 6 */ {0xF4, 0xDA, 0x06, 0xDB, 0xBF, 0x4E, 0x6F, 0xB3},
        /* Col 7 */ {0x9E, 0x08, 0xD1, 0xAE, 0x59, 0x5E, 0xE8, 0xF0},
        /* Col 8 */ {0xC0, 0x90, 0x8F, 0xBB, 0x7C, 0x8E, 0x2B, 0x8E}
                    // {0,0,0,0,0,0,0,0}
      },
      { /* Row 3 */
        /* Col 0 */ {0xC0, 0x90, 0x8F, 0xBB, 0x7C, 0x8E, 0x2B, 0x8E},
        /* Col 1 */ {0x80, 0x69, 0x26, 0x80, 0x08, 0xF8, 0x49, 0xE7},
        /* Col 2 */ {0x7D, 0x2D, 0x49, 0x54, 0xD0, 0x80, 0x40, 0xC1},
        /* Col 3 */ {0xB6, 0xF2, 0xE6, 0x1B, 0x80, 0x5A, 0x36, 0xB4},
        /* Col 4 */ {0x42, 0xAE, 0x9C, 0x1C, 0xDA, 0x67, 0x05, 0xF6},
        /* Col 5 */ {0x9B, 0x75, 0xF7, 0xE0, 0x14, 0x8D, 0xB5, 0x80},
        /* Col 6 */ {0xBF, 0x54, 0x98, 0xB9, 0xB7, 0x30, 0x5A, 0x88},
        /* Col 7 */ {0x35, 0xD1, 0xFC, 0x97, 0x23, 0xD4, 0xC9, 0x88},
        /* Col 8 */ {0xE1, 0xD6, 0x31, 0x26, 0x5F, 0xBD, 0x40, 0x93}
                    // {0,0,0,0,0,0,0,0}
      },
      { /* Row 4 */
        /* Col 0 */ {0xE1, 0xD6, 0x31, 0x26, 0x5F, 0xBD, 0x40, 0x93},
        /* Col 1 */ {0xDC, 0x68, 0x08, 0x99, 0x97, 0xAE, 0xAF, 0x8C},
        /* Col 2 */ {0xC3, 0x0E, 0x01, 0x16, 0x0E, 0x32, 0x06, 0xBA},
        /* Col 3 */ {0xE0, 0x83, 0x01, 0xFA, 0xAB, 0x3E, 0x8F, 0xAC},
        /* Col 4 */ {0x5C, 0xD5, 0x9C, 0xB8, 0x46, 0x9C, 0x7D, 0x84},
        /* Col 5 */ {0xF1, 0xC6, 0xFE, 0x5C, 0x9D, 0xA5, 0x4F, 0xB7},
        /* Col 6 */ {0x58, 0xB5, 0xB3, 0xDD, 0x0E, 0x28, 0xF1, 0xB0},
        /* Col 7 */ {0x5F, 0x30, 0x3B, 0x56, 0x96, 0x45, 0xF4, 0xA1},
        /* Col 8 */ {0x03, 0xBC, 0x6E, 0x8A, 0xEF, 0xBD, 0xFE, 0xF8}
      },
    };

    
  } // namespace dsmx
} // namespace gr

#endif /* INCLUDED_DSMX_DESPREADER_IMPL_H */

