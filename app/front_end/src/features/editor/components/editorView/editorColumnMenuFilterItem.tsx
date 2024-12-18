import { FilterAlt as FilterAltIcon } from '@mui/icons-material';
import { Box, FormControl, InputLabel, MenuItem, OutlinedInput, Select, SelectChangeEvent, Typography, useTheme } from '@mui/material';
import { FilterEnum } from '@/features/editor/types';
import { SyntheticEvent, useState } from 'react';

export interface EditorColumnMenuFilterItemProps {
    onClick: (event:  SyntheticEvent<Element, Event>) => void;
    onFilter: (operator: FilterEnum) => void;
}

export const EditorColumnMenuFilterItem: React.FC<EditorColumnMenuFilterItemProps> = ({}) => {
  const Theme = useTheme();

  const [operator, setOperator] = useState<FilterEnum>(FilterEnum.CONTAINS);

  const handleChange = (event: SelectChangeEvent) => {
    const operator = event.target.value as FilterEnum;
    setOperator(operator);
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'row',
        gap: '1rem',
        alignItems: 'center',
        px: '0.85rem',
        py: '1rem',
      }}
    >
      <FilterAltIcon sx={{ color: Theme.palette.text.secondary }} />
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          width: '100%',
          gap: '1rem',
          alignItems: 'center',
        }}
      >
        <FormControl fullWidth size='small'>
          <InputLabel>
            <Box 
              sx={{
                bgcolor: Theme.palette.background.default,
                pr: '0.5rem',
              }}
            >
              <Typography>Operator</Typography>
            </Box>
          </InputLabel>
          <Select
            id='filter-operator'
            label='Operator'
            value={operator}
            onChange={handleChange}
            size='small'
            sx={{
              fontSize: '0.8rem',
            }}
          >
            <MenuItem value={FilterEnum.CONTAINS}>
              contains
            </MenuItem>
            <MenuItem value={FilterEnum.NOT_CONTAINS}>
              does not contain
            </MenuItem>
            <MenuItem value={FilterEnum.EQUALS}>
              equals
            </MenuItem>
            <MenuItem value={FilterEnum.NOT_EQUALS}>
              does not equal
            </MenuItem>
            <MenuItem value={FilterEnum.STARTS}>
              starts with
            </MenuItem>
            <MenuItem value={FilterEnum.ENDS}>
              ends with
            </MenuItem>
            <MenuItem value={FilterEnum.EMPTY}>
              is empty
            </MenuItem>
            <MenuItem value={FilterEnum.NOT_EMPTY}>
              is not empty
            </MenuItem>
          </Select>
        </FormControl>
        <FormControl fullWidth size='small'>
          <InputLabel>
            <Box 
              sx={{
                bgcolor: Theme.palette.background.default,
                pr: '0.5rem',
              }}
            >
              <Typography>Value</Typography>
            </Box>
          </InputLabel>
          <OutlinedInput
            id='filter-value'
            label="Value"
            size='small'
            sx={{
              fontSize: '0.8rem',
              '.MuiOutlinedInput-notchedOutline': {
                  borderColor: '#404040',
              },
              '&:hover .MuiOutlinedInput-notchedOutline': {
                borderColor: '#4C7380',
              },
            }}
          >
          </OutlinedInput>
        </FormControl>
      </Box>
    </Box>
  );
};
