"""
StormSight — Shared Spatiotemporal Encoder

Backbone architecture for the multi-task severe weather nowcasting model.
Supports ConvLSTM and ConvGRU variants.

TODO:
- [ ] Implement ConvLSTM cell
- [ ] Implement ConvGRU cell
- [ ] Build shared encoder that processes [B, T, C, H, W] input sequences
- [ ] Output shared representation for multi-task heads
"""

import torch
import torch.nn as nn


class ConvLSTMCell(nn.Module):
    """Single ConvLSTM cell — preserves spatial structure through time."""

    def __init__(self, input_channels: int, hidden_channels: int, kernel_size: int = 3):
        super().__init__()
        self.hidden_channels = hidden_channels
        padding = kernel_size // 2

        # Gates: input, forget, output, cell candidate — all in one conv
        self.gates = nn.Conv2d(
            input_channels + hidden_channels,
            4 * hidden_channels,
            kernel_size=kernel_size,
            padding=padding,
        )

    def forward(self, x, h_prev, c_prev):
        """
        Args:
            x: [B, C_in, H, W]
            h_prev: [B, C_hidden, H, W]
            c_prev: [B, C_hidden, H, W]
        Returns:
            h_next, c_next
        """
        combined = torch.cat([x, h_prev], dim=1)
        gates = self.gates(combined)

        i, f, o, g = gates.chunk(4, dim=1)
        i = torch.sigmoid(i)
        f = torch.sigmoid(f)
        o = torch.sigmoid(o)
        g = torch.tanh(g)

        c_next = f * c_prev + i * g
        h_next = o * torch.tanh(c_next)

        return h_next, c_next


class SpatiotemporalBackbone(nn.Module):
    """
    Shared spatiotemporal encoder for multi-task severe weather prediction.

    Input: [B, T, C, H, W] — sequence of T frames, each with C channels
    Output: [B, hidden_dim, H', W'] — shared spatial feature map
    """

    def __init__(
        self,
        input_channels: int,
        hidden_channels: int = 64,
        num_layers: int = 2,
    ):
        super().__init__()
        # TODO: Implement full backbone
        # 1. Per-frame CNN encoder
        # 2. ConvLSTM temporal processing
        # 3. Output shared representation
        raise NotImplementedError("Implement the backbone architecture")


# TODO: Add ConvGRU variant as alternative
