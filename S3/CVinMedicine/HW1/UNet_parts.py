import torch
import torch.nn as nn

class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv_op = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size = 3, padding = 1), # padding =  1 Normally not in the paper but output result will be the same as the input
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size = 3, padding = 1),
            nn.ReLU(inplace=True),
        )
    def forward(self, x):
        return self.conv_op(x)

class DownSample(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv = DoubleConv(in_channels, out_channels)
        self.pool = nn.MaxPool2d(kernel_size = 2, stride = 2)
    
    def forward(self, x):
        down = self.conv(x)
        p = self.pool(down)
        return down, p
class Upsample(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.up = nn.ConvTranspose2d(in_channels, in_channels//2, kernel_size = 2, stride = 2)
        self.conv = DoubleConv(in_channels, out_channels)
    def forward(self, x1, x2):
        x1 = self.up(x1)
        
        '''
        This here fixes the problem if the input size is not divisable 16
        Instead of stopping the whole process, I just get a smaller sized output.
        572x572 -> 560x560 Should still be okay but been bothering me so I added it
        '''
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]
        start_y = diffY // 2
        start_x = diffX // 2
        
        end_y = x2.size()[2] - (diffY - diffY // 2)
        end_x = x2.size()[3] - (diffX - diffX // 2)
        x2_cropped = x2[:, :, start_y:end_y, start_x:end_x]
        
        x = torch.cat([x2_cropped, x1], dim = 1)
        return self.conv(x)