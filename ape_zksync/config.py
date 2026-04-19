from ape_ethereum.ecosystem import NetworkConfig
from ape.api.config import PluginConfig


class ZkSyncConfig(PluginConfig):
    era_sepolia: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=1)  # type: ignore
    era_mainnet: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=1)  # type: ignore
    default_network: str = "era-sepolia"
