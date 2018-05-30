# -*- coding: utf-8; -*-
#
# Copyright (C) 2016  DING Changchang (of Canaan Creative)
#
# This file is part of Avalon Management System (AMS).
#
# AMS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AMS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AMS. If not, see <http://www.gnu.org/licenses/>.

import re
import datetime

import ams.miner as miner


class Miner(miner.Miner):
    _pattern = re.compile(
        r'Ver\[(?P<Ver>[-0-9A-Fa-f+]+)\]\s'
        'DNA\[(?P<DNA>[0-9A-Fa-f]+)\]\s'
        'Elapsed\[(?P<Elapsed>[-0-9]+)\]\s'
        'MW\[(?P<MW>[-\s0-9]+)\]\s'
        'LW\[(?P<LW>[-0-9]+)\]\s'
        'MH\[(?P<MH>[-\s0-9]+)\]\s'
        'HW\[(?P<HW>[-0-9]+)\]\s'
        'Temp\[(?P<Temp>[0-9]+)\]\s'
        'TMax\[(?P<TMax>[0-9]+)\]\s'
        'Fan\[(?P<Fan>[0-9]+)\]\s'
        'FanR\[(?P<FanR>[0-9]+)%\]\s'
        'Vi\[(?P<Vi>[-\s0-9]+)\]\s'
        'Vo\[(?P<Vo>[-\s0-9]+)\]\s'
        '('
        'PLL0\[(?P<PLL0>[-\s0-9]+)\]\s'
        'PLL1\[(?P<PLL1>[-\s0-9]+)\]\s'
        'PLL2\[(?P<PLL2>[-\s0-9]+)\]\s'
        'PLL3\[(?P<PLL3>[-\s0-9]+)\]\s'
        ')?'
        'GHSmm\[(?P<GHSmm>[-.0-9]+)\]\s'
        'WU\[(?P<WU>[-.0-9]+)\]\s'
        'Freq\[(?P<Freq>[.0-9]+)\]\s'
        'PG\[(?P<PG>[0-9]+)\]\s'
        'Led\[(?P<LED>0|1)\]\s'
        'MW0\[(?P<MW0>[0-9\s]+)\]\s'
        'MW1\[(?P<MW1>[0-9\s]+)\]\s'
        'MW2\[(?P<MW2>[0-9\s]+)\]\s'
        'MW3\[(?P<MW3>[0-9\s]+)\]\s'
        'TA\[(?P<TA>[0-9]+)\]\s'
        'ECHU\[(?P<ECHU>[0-9\s]+)\]\s'
        'ECMM\[(?P<ECMM>[0-9]+)\]\s.*'
        'FAC0\[(?P<FAC0>[-0-9]+)\]\s'
        'OC\[(?P<OC>[0-9]+)\]\s'
        'SF0\[(?P<SF0>[-\s0-9]+)\]\s'
        'SF1\[(?P<SF1>[-\s0-9]+)\]\s'
        'SF2\[(?P<SF2>[-\s0-9]+)\]\s'
        'SF3\[(?P<SF3>[-\s0-9]+)\]\s'
        'PMUV\[(?P<PMUV>[-\s\S*]+)\]\s'
        'PVT_T0\[(?P<PVT_T0>[-0-9\s]+)\]\s'
        'PVT_T1\[(?P<PVT_T1>[-0-9\s]+)\]\s'
        'PVT_T2\[(?P<PVT_T2>[-0-9\s]+)\]\s'
        'PVT_T3\[(?P<PVT_T3>[-0-9\s]+)\]\s'
        'PVT_V0_0\[(?P<PVT_V0_0>[-0-9\s]+)\]\s'
        'PVT_V0_1\[(?P<PVT_V0_1>[-0-9\s]+)\]\s'
        'PVT_V0_2\[(?P<PVT_V0_2>[-0-9\s]+)\]\s'
        'PVT_V0_3\[(?P<PVT_V0_3>[-0-9\s]+)\]\s'
        'PVT_V0_4\[(?P<PVT_V0_4>[-0-9\s]+)\]\s'
        'PVT_V0_5\[(?P<PVT_V0_5>[-0-9\s]+)\]\s'
        'PVT_V0_6\[(?P<PVT_V0_6>[-0-9\s]+)\]\s'
        'PVT_V0_7\[(?P<PVT_V0_7>[-0-9\s]+)\]\s'
        'PVT_V0_8\[(?P<PVT_V0_8>[-0-9\s]+)\]\s'
        'PVT_V0_9\[(?P<PVT_V0_9>[-0-9\s]+)\]\s'
        'PVT_V0_10\[(?P<PVT_V0_10>[-0-9\s]+)\]\s'
        'PVT_V0_11\[(?P<PVT_V0_11>[-0-9\s]+)\]\s'
        'PVT_V0_12\[(?P<PVT_V0_12>[-0-9\s]+)\]\s'
        'PVT_V0_13\[(?P<PVT_V0_13>[-0-9\s]+)\]\s'
        'PVT_V0_14\[(?P<PVT_V0_14>[-0-9\s]+)\]\s'
        'PVT_V0_15\[(?P<PVT_V0_15>[-0-9\s]+)\]\s'
        'PVT_V0_16\[(?P<PVT_V0_16>[-0-9\s]+)\]\s'
        'PVT_V0_17\[(?P<PVT_V0_17>[-0-9\s]+)\]\s'
        'PVT_V0_18\[(?P<PVT_V0_18>[-0-9\s]+)\]\s'
        'PVT_V0_19\[(?P<PVT_V0_19>[-0-9\s]+)\]\s'
        'PVT_V0_20\[(?P<PVT_V0_20>[-0-9\s]+)\]\s'
        'PVT_V0_21\[(?P<PVT_V0_21>[-0-9\s]+)\]\s'
        'PVT_V0_22\[(?P<PVT_V0_22>[-0-9\s]+)\]\s'
        'PVT_V0_23\[(?P<PVT_V0_23>[-0-9\s]+)\]\s'
        'PVT_V0_24\[(?P<PVT_V0_24>[-0-9\s]+)\]\s'
        'PVT_V0_25\[(?P<PVT_V0_25>[-0-9\s]+)\]\s'
        'PVT_V1_0\[(?P<PVT_V1_0>[-0-9\s]+)\]\s'
        'PVT_V1_1\[(?P<PVT_V1_1>[-0-9\s]+)\]\s'
        'PVT_V1_2\[(?P<PVT_V1_2>[-0-9\s]+)\]\s'
        'PVT_V1_3\[(?P<PVT_V1_3>[-0-9\s]+)\]\s'
        'PVT_V1_4\[(?P<PVT_V1_4>[-0-9\s]+)\]\s'
        'PVT_V1_5\[(?P<PVT_V1_5>[-0-9\s]+)\]\s'
        'PVT_V1_6\[(?P<PVT_V1_6>[-0-9\s]+)\]\s'
        'PVT_V1_7\[(?P<PVT_V1_7>[-0-9\s]+)\]\s'
        'PVT_V1_8\[(?P<PVT_V1_8>[-0-9\s]+)\]\s'
        'PVT_V1_9\[(?P<PVT_V1_9>[-0-9\s]+)\]\s'
        'PVT_V1_10\[(?P<PVT_V1_10>[-0-9\s]+)\]\s'
        'PVT_V1_11\[(?P<PVT_V1_11>[-0-9\s]+)\]\s'
        'PVT_V1_12\[(?P<PVT_V1_12>[-0-9\s]+)\]\s'
        'PVT_V1_13\[(?P<PVT_V1_13>[-0-9\s]+)\]\s'
        'PVT_V1_14\[(?P<PVT_V1_14>[-0-9\s]+)\]\s'
        'PVT_V1_15\[(?P<PVT_V1_15>[-0-9\s]+)\]\s'
        'PVT_V1_16\[(?P<PVT_V1_16>[-0-9\s]+)\]\s'
        'PVT_V1_17\[(?P<PVT_V1_17>[-0-9\s]+)\]\s'
        'PVT_V1_18\[(?P<PVT_V1_18>[-0-9\s]+)\]\s'
        'PVT_V1_19\[(?P<PVT_V1_19>[-0-9\s]+)\]\s'
        'PVT_V1_20\[(?P<PVT_V1_20>[-0-9\s]+)\]\s'
        'PVT_V1_21\[(?P<PVT_V1_21>[-0-9\s]+)\]\s'
        'PVT_V1_22\[(?P<PVT_V1_22>[-0-9\s]+)\]\s'
        'PVT_V1_23\[(?P<PVT_V1_23>[-0-9\s]+)\]\s'
        'PVT_V1_24\[(?P<PVT_V1_24>[-0-9\s]+)\]\s'
        'PVT_V1_25\[(?P<PVT_V1_25>[-0-9\s]+)\]\s'
        'PVT_V2_0\[(?P<PVT_V2_0>[-0-9\s]+)\]\s'
        'PVT_V2_1\[(?P<PVT_V2_1>[-0-9\s]+)\]\s'
        'PVT_V2_2\[(?P<PVT_V2_2>[-0-9\s]+)\]\s'
        'PVT_V2_3\[(?P<PVT_V2_3>[-0-9\s]+)\]\s'
        'PVT_V2_4\[(?P<PVT_V2_4>[-0-9\s]+)\]\s'
        'PVT_V2_5\[(?P<PVT_V2_5>[-0-9\s]+)\]\s'
        'PVT_V2_6\[(?P<PVT_V2_6>[-0-9\s]+)\]\s'
        'PVT_V2_7\[(?P<PVT_V2_7>[-0-9\s]+)\]\s'
        'PVT_V2_8\[(?P<PVT_V2_8>[-0-9\s]+)\]\s'
        'PVT_V2_9\[(?P<PVT_V2_9>[-0-9\s]+)\]\s'
        'PVT_V2_10\[(?P<PVT_V2_10>[-0-9\s]+)\]\s'
        'PVT_V2_11\[(?P<PVT_V2_11>[-0-9\s]+)\]\s'
        'PVT_V2_12\[(?P<PVT_V2_12>[-0-9\s]+)\]\s'
        'PVT_V2_13\[(?P<PVT_V2_13>[-0-9\s]+)\]\s'
        'PVT_V2_14\[(?P<PVT_V2_14>[-0-9\s]+)\]\s'
        'PVT_V2_15\[(?P<PVT_V2_15>[-0-9\s]+)\]\s'
        'PVT_V2_16\[(?P<PVT_V2_16>[-0-9\s]+)\]\s'
        'PVT_V2_17\[(?P<PVT_V2_17>[-0-9\s]+)\]\s'
        'PVT_V2_18\[(?P<PVT_V2_18>[-0-9\s]+)\]\s'
        'PVT_V2_19\[(?P<PVT_V2_19>[-0-9\s]+)\]\s'
        'PVT_V2_20\[(?P<PVT_V2_20>[-0-9\s]+)\]\s'
        'PVT_V2_21\[(?P<PVT_V2_21>[-0-9\s]+)\]\s'
        'PVT_V2_22\[(?P<PVT_V2_22>[-0-9\s]+)\]\s'
        'PVT_V2_23\[(?P<PVT_V2_23>[-0-9\s]+)\]\s'
        'PVT_V2_24\[(?P<PVT_V2_24>[-0-9\s]+)\]\s'
        'PVT_V2_25\[(?P<PVT_V2_25>[-0-9\s]+)\]\s'
        'PVT_V3_0\[(?P<PVT_V3_0>[-0-9\s]+)\]\s'
        'PVT_V3_1\[(?P<PVT_V3_1>[-0-9\s]+)\]\s'
        'PVT_V3_2\[(?P<PVT_V3_2>[-0-9\s]+)\]\s'
        'PVT_V3_3\[(?P<PVT_V3_3>[-0-9\s]+)\]\s'
        'PVT_V3_4\[(?P<PVT_V3_4>[-0-9\s]+)\]\s'
        'PVT_V3_5\[(?P<PVT_V3_5>[-0-9\s]+)\]\s'
        'PVT_V3_6\[(?P<PVT_V3_6>[-0-9\s]+)\]\s'
        'PVT_V3_7\[(?P<PVT_V3_7>[-0-9\s]+)\]\s'
        'PVT_V3_8\[(?P<PVT_V3_8>[-0-9\s]+)\]\s'
        'PVT_V3_9\[(?P<PVT_V3_9>[-0-9\s]+)\]\s'
        'PVT_V3_10\[(?P<PVT_V3_10>[-0-9\s]+)\]\s'
        'PVT_V3_11\[(?P<PVT_V3_11>[-0-9\s]+)\]\s'
        'PVT_V3_12\[(?P<PVT_V3_12>[-0-9\s]+)\]\s'
        'PVT_V3_13\[(?P<PVT_V3_13>[-0-9\s]+)\]\s'
        'PVT_V3_14\[(?P<PVT_V3_14>[-0-9\s]+)\]\s'
        'PVT_V3_15\[(?P<PVT_V3_15>[-0-9\s]+)\]\s'
        'PVT_V3_16\[(?P<PVT_V3_16>[-0-9\s]+)\]\s'
        'PVT_V3_17\[(?P<PVT_V3_17>[-0-9\s]+)\]\s'
        'PVT_V3_18\[(?P<PVT_V3_18>[-0-9\s]+)\]\s'
        'PVT_V3_19\[(?P<PVT_V3_19>[-0-9\s]+)\]\s'
        'PVT_V3_20\[(?P<PVT_V3_20>[-0-9\s]+)\]\s'
        'PVT_V3_21\[(?P<PVT_V3_21>[-0-9\s]+)\]\s'
        'PVT_V3_22\[(?P<PVT_V3_22>[-0-9\s]+)\]\s'
        'PVT_V3_23\[(?P<PVT_V3_23>[-0-9\s]+)\]\s'
        'PVT_V3_24\[(?P<PVT_V3_24>[-0-9\s]+)\]\s'
        'PVT_V3_25\[(?P<PVT_V3_25>[-0-9\s]+)\]\s'
        'FM\[(?P<FM>[0-9]+)\]\s'
        'CRC\[(?P<CRC>[0-9\s]+)\]', re.X
    )

    name = 'Avalon8'

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()

    def _collect(self, *args, **kwargs):
        return super()._collect(*args, **kwargs)

    def _generate_sql_summary(self, run_time):
        # 'summary' -> table 'miner'
        try:
            summary = self.raw['summary']['SUMMARY'][0]
        except (TypeError, KeyError):
            self.sql_queue.put({
                'command': 'insert',
                'name': 'miner_temp',
                'column': ['time', 'ip', 'port',
                           'precise_time', 'total_mh', 'dead'],
                'value': [run_time, self.ip, self.port, run_time, 0, 1],
            })
            return

        summary['Last getwork'] = datetime.datetime.fromtimestamp(
            summary['Last getwork']
        )

        precise_time = datetime.datetime.fromtimestamp(
            self.raw['summary']['STATUS'][0]['When']
        )

        summary_sorted = sorted(summary)
        column = ['time', 'ip', 'port', 'precise_time']
        column.extend(
            k.strip('%').replace(' ', '_').lower() for k in summary_sorted
        )
        value = [run_time, self.ip, self.port, precise_time]
        value.extend(summary[k] for k in summary_sorted)
        try:
            self.sql_queue.put({
                'command': 'insert',
                'name': 'miner_temp',
                'column': column,
                'value': value
            })
        except:
            self.sql_queue.append({
                'command': 'insert',
                'name': 'miner_temp',
                'column': column,
                'value': value
            })

    def _generate_sql_edevs(self, run_time):
        # 'edevs' -> table 'device'
        # 'estats' -> table 'module'
        try:
            edevs = self.raw['edevs']['DEVS']
            estats = self.raw['estats']['STATS']
        except (TypeError, KeyError):
            return

        precise_time = datetime.datetime.fromtimestamp(
            self.raw['edevs']['STATUS'][0]['When']
        )
        column = ['time', 'ip', 'port', 'precise_time', 'device_id']
        value = [run_time, self.ip, self.port, precise_time]
        i = 0
        for edev in edevs:
            edev_sorted = sorted(edev)
            new_column = [k.strip('%').replace(' ', '_').lower()
                          for k in edev_sorted]
            edev['Last Share Time'] = datetime.datetime.fromtimestamp(
                edev['Last Share Time']
            )
            edev['Last Valid Work'] = datetime.datetime.fromtimestamp(
                edev['Last Valid Work']
            )

            new_value = [edev['ID']]
            new_value.extend(edev[k] for k in edev_sorted)
            estat = estats[i]
            new_column.extend(
                k.replace(' ', '_').lower() for k in sorted(estat)
                if k.replace(' ', '_').lower() in [
                    'mm_count',
                    'smart_speed',
                    'auc_ver',
                    'auc_i2c_speed',
                    'auc_i2c_xdelay',
                    'auc_sensor',
                    'auc_temperature',
                    'usb_pipe',
                    'usb_delay',
                    'usb_tmo'
                ]
            )
            new_value.extend(
                estat[k] for k in sorted(estat)
                if k.replace(' ', '_').lower() in [
                    'mm_count',
                    'smart_speed',
                    'auc_ver',
                    'auc_i2c_speed',
                    'auc_i2c_xdelay',
                    'auc_sensor',
                    'auc_temperature',
                    'usb_pipe',
                    'usb_delay',
                    'usb_tmo'
                ]
            )
            try:
                self.sql_queue.put({
                    'command': 'insert',
                    'name': 'device_temp',
                    'column': column + new_column,
                    'value': value + new_value
                })
            except:
                self.sql_queue.append({
                    'command': 'insert',
                    'name': 'device_temp',
                    'column': column + new_column,
                    'value': value + new_value
                })
            i += 1

    def _generate_sql_estats(self, run_time):
        # 'estats' -> table 'module'
        try:
            estats = self.raw['estats']['STATS']
        except (TypeError, KeyError):
            return

        precise_time = datetime.datetime.fromtimestamp(
            self.raw['estats']['STATUS'][0]['When']
        )
        column = ['time', 'ip', 'port', 'precise_time',
                  'device_id', 'module_id']
        value = [run_time, self.ip, self.port, precise_time]
        for estat in estats:
            for key in estat:
                if key[:5] == 'MM ID':
                    self._generate_sql_estat(column, value, key, estat)

    def _generate_sql_estat(self, column, value, key, estat):
        device_id = int(estat['ID'][3:])
        module_id = int(key[5:])
        module = estat[key]
        module_info = re.match(self._pattern, module)
        if module_info is None:
            if not self.log:
                return
            self.log.error('{}[{}][{}] Non-match module info.'.format(
                self, device_id, module_id
            ))
            #self.log.debug('{}[{}][{}] {}'.format(
            #    self, device_id, module_id, module
            #))
            return

        module_info = module_info.groupdict()
        new_column = []
        new_value = [device_id, module_id]
        for k in module_info:
            if (k == 'DNA' or k == 'Ver' or
                    k == 'LED' or k == 'Elapsed' or k == 'FAC0'):
                new_column.append(k.lower())
                new_value.append(module_info[k])
            elif (k == 'Freq' or k == 'WU' or
                  k == 'GHSmm'):
                new_column.append(k.lower())
                new_value.append(float(module_info[k]))
            elif (k in ['MW', 'MH', 'Vi',
                        'Vo', 'ECHU', 'CRC', 'PMUV'] or
                  k[:-1] in ['PLL', 'SF', 'MW'] or
                  k[:5] == 'PVT_T') and module_info[k] is not None:
                for i, m in enumerate(module_info[k].split()):
                    new_column.append('{}_{}'.format(k.lower(), i))
                    if k == 'PMUV':
                        new_value.append(m)
                    else:
                        new_value.append(int(m))
            elif (k[:5] == 'PVT_V') and module_info[k] is not None:
                new_column.append(k.lower())
                new_value.append(module_info[k])
            elif module_info[k] is not None:
                new_column.append(k.lower())
                new_value.append(int(module_info[k]))

        try:
            self.sql_queue.put({
                'command': 'insert',
                'name': 'module_temp',
                'column': column + new_column,
                'value': value + new_value
            })
        except:
            self.sql_queue.append({
                'command': 'insert',
                'name': 'module_temp',
                'column': column + new_column,
                'value': value + new_value
            })

    def _generate_sql_pools(self, run_time):
        # 'pools' -> table 'pool'
        try:
            pools = self.raw['pools']['POOLS']
        except (TypeError, KeyError):
            return

        precise_time = datetime.datetime.fromtimestamp(
            self.raw['pools']['STATUS'][0]['When']
        )
        column = ['time', 'ip', 'port', 'precise_time', 'pool_id']
        value = [run_time, self.ip, self.port, precise_time]
        for pool in pools:
            pool_sorted = sorted(pool)
            pool['Last Share Time'] = datetime.datetime.fromtimestamp(
                pool['Last Share Time']
            )
            new_column = [k.strip('%').replace(' ', '_').lower()
                          for k in pool_sorted]
            new_value = [pool['POOL']]
            new_value.extend(pool[k] for k in pool_sorted)
            try:
                self.sql_queue.put({
                    'command': 'insert',
                    'name': 'pool_temp',
                    'column': column + new_column,
                    'value': value + new_value
                })
            except:
                self.sql_queue.append({
                    'command': 'insert',
                    'name': 'pool_temp',
                    'column': column + new_column,
                    'value': value + new_value
                })

    def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)


COLUMN_EDEVS = [
    {'name': 'time',
     'type': 'TIMESTAMP DEFAULT 0'},
    {'name': 'ip',
     'type': 'VARCHAR(40)'},
    {'name': 'port',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'precise_time',
     'type': 'TIMESTAMP DEFAULT 0'},
    {'name': 'device_id',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'asc',
     'type': 'INT'},
    {'name': 'name',
     'type': 'CHAR(3)'},
    {'name': 'id',
     'type': 'INT'},
    {'name': 'enabled',
     'type': 'CHAR(1)'},
    {'name': 'status',
     'type': 'CHAR(1)'},
    {'name': 'temperature',
     'type': 'DOUBLE'},
    {'name': 'mhs_av',
     'type': 'DOUBLE'},
    {'name': 'mhs_5s',
     'type': 'DOUBLE'},
    {'name': 'mhs_1m',
     'type': 'DOUBLE'},
    {'name': 'mhs_5m',
     'type': 'DOUBLE'},
    {'name': 'mhs_15m',
     'type': 'DOUBLE'},
    {'name': 'accepted',
     'type': 'INT'},
    {'name': 'rejected',
     'type': 'INT'},
    {'name': 'hardware_errors',
     'type': 'INT'},
    {'name': 'utility',
     'type': 'DOUBLE'},
    {'name': 'last_share_pool',
     'type': 'INT'},
    {'name': 'last_share_time',
     'type': 'TIMESTAMP DEFAULT 0'},
    {'name': 'total_mh',
     'type': 'DOUBLE'},
    {'name': 'diff1_work',
     'type': 'BIGINT'},
    {'name': 'difficulty_accepted',
     'type': 'DOUBLE'},
    {'name': 'difficulty_rejected',
     'type': 'DOUBLE'},
    {'name': 'last_share_difficulty',
     'type': 'DOUBLE'},
    {'name': 'no_device',
     'type': 'BOOL'},
    {'name': 'last_valid_work',
     'type': 'TIMESTAMP DEFAULT 0'},
    {'name': 'device_hardware',
     'type': 'DOUBLE'},
    {'name': 'device_rejected',
     'type': 'DOUBLE'},
    {'name': 'device_elapsed',
     'type': 'BIGINT'},
    {'name': 'mm_count',
     'type': 'INT'},
    {'name': 'smart_speed',
     'type': 'BOOL'},
    {'name': 'automatic_voltage',
     'type': 'BOOL'},
    {'name': 'auc_ver',
     'type': 'CHAR(12)'},
    {'name': 'auc_i2c_speed',
     'type': 'INT'},
    {'name': 'auc_i2c_xdelay',
     'type': 'INT'},
    {'name': 'auc_sensor',
     'type': 'INT'},
    {'name': 'auc_temperature',
     'type': 'DOUBLE'},
    {'name': 'usb_pipe',
     'type': 'VARCHAR(32)'},
    {'name': 'usb_delay',
     'type': 'VARCHAR(32)'},
    {'name': 'usb_tmo',
     'type': 'VARCHAR(32)'}
]

COLUMN_ESTATS = [
    {'name': 'time',
     'type': 'TIMESTAMP DEFAULT 0'},
    {'name': 'ip',
     'type': 'VARCHAR(40)'},
    {'name': 'port',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'precise_time',
     'type': 'TIMESTAMP DEFAULT 0'},
    {'name': 'device_id',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'module_id',
     'type': 'TINYINT UNSIGNED'},
    {'name': 'ver',
     'type': 'CHAR(15)'},
    {'name': 'dna',
     'type': 'CHAR(16)'},
    {'name': 'elapsed',
     'type': 'BIGINT'},
    {'name': 'lw',
     'type': 'BIGINT'},
    {'name': 'hw',
     'type': 'BIGINT'},
    {'name': 'dh',
     'type': 'DOUBLE'},
    {'name': 'temp',
     'type': 'INT'},
    {'name': 'tmax',
     'type': 'INT'},
    {'name': 'fan',
     'type': 'INT'},
    {'name': 'fanr',
     'type': 'INT'},
    {'name': 'ghsmm',
     'type': 'DOUBLE'},
    {'name': 'wu',
     'type': 'DOUBLE'},
    {'name': 'freq',
     'type': 'DOUBLE'},
    {'name': 'pg',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'led',
     'type': 'BOOL'},
    {'name': 'ta',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'ecmm',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'fac0',
     'type': 'SMALLINT UNSIGNED'},
     {'name': 'oc',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'fm',
     'type': 'SMALLINT UNSIGNED'},
    {'name': 'pmuv_0',
     'type': 'CHAR(4)'},
    {'name': 'pmuv_1',
     'type': 'CHAR(4)'},
]

for i in range(4):
    for j in range(26):
        COLUMN_ESTATS.append({
            'name': 'pvt_t{}_{}'.format(i, j),
            'type': 'INT',
        })
    for name in ['mw', 'mh', 'vi', 'vo', 'echu', 'crc']:
        COLUMN_ESTATS.append({
            'name': '{}_{}'.format(name, i),
            'type': 'INT',
        })
    for j in range(4):
        for name in ['pll', 'sf']:
            COLUMN_ESTATS.append({
                'name': '{}{}_{}'.format(name, i, j),
                'type': 'INT',
            })
    for j in range(26):
        COLUMN_ESTATS.append({
            'name': 'mw{}_{}'.format(i, j),
            'type': 'INT',
        })
    for j in range(26):
        COLUMN_ESTATS.append({
            'name': 'PVT_V{}_{}'.format(i, j),
            'type': 'VARCHAR(255)'
            })

def db_init(sql_queue):
    miner.db_init(sql_queue)
    #print(sql_queue.qsize())
    for suffix in ['', '_temp']:
        sql_queue.put({
            'command': 'create',
            'name': 'device{}'.format(suffix),
            'column_def': COLUMN_EDEVS,
            'additional': 'PRIMARY KEY(`time`, `ip`, `port`, `device_id`)',
        })
        sql_queue.put({
            'command': 'create',
            'name': 'module{}'.format(suffix),
            'column_def': COLUMN_ESTATS,
            'additional': 'PRIMARY KEY(\
                `time`, `ip`, `port`, `device_id`, `module_id`\
            )',
        })
    #print(sql_queue.qsize())


def db_final(sql_queue, run_time):
    sql_queue.put({
        'command': 'raw',
        'query': '''
UPDATE miner_temp AS a
  LEFT OUTER JOIN (
           SELECT time, ip, port, precise_time, elapsed, total_mh
             FROM miner
            WHERE time = (SELECT MAX(time) FROM miner)
       ) b
    ON a.ip = b.ip and a.port = b.port
   SET mhs = IF(
         a.precise_time > b.precise_time
             AND TIMESTAMPDIFF(SECOND, b.precise_time, a.precise_time)
                     >= a.elapsed - b.elapsed - 1
             AND TIMESTAMPDIFF(SECOND, b.precise_time, a.precise_time)
                     <= a.elapsed - b.elapsed + 1,
         (a.total_mh - b.total_mh) / (a.elapsed - b.elapsed),
         a.total_mh / a.elapsed
       )
        ''',
    })
    for name in ['miner', 'device', 'module', 'pool']:
        sql_queue.put({
            'command': 'raw',
            'query': 'REPLACE INTO {0} SELECT * FROM {0}_temp'.format(name),
        })
    sql_queue.put({
        'command': 'raw',
        'query': 'DROP TABLES miner_temp, device_temp, module_temp, pool_temp',
    })

    sql_queue.put({
        'command': 'raw',
        'query': '''\
INSERT INTO hashrate (time, local)
VALUES ("{0}", (SELECT sum(mhs) FROM miner WHERE time="{0}"))
    ON DUPLICATE KEY UPDATE
       local=(SELECT sum(mhs) FROM miner WHERE time="{0}")'''.format(run_time)
    })
