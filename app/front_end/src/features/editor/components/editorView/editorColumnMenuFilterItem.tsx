import { FilterAlt as FilterAltIcon } from '@mui/icons-material';
import { Box, FormControl, InputLabel, MenuItem, OutlinedInput, Select, Typography, useTheme } from '@mui/material';

export interface EditorColumnMenuFilterItemProps {}

export const EditorColumnMenuFilterItem: React.FC<EditorColumnMenuFilterItemProps> = ({}) => {
  const Theme = useTheme();

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
            size='small'
            sx={{
              fontSize: '0.8rem',
            }}
          >
            <MenuItem>
              ...
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
