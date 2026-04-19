"""
Functional tests for ZkSyncProvider.
Run against a real Era Sepolia connection:
    ape test --network zksync:era-sepolia:zksync
"""
import pytest


@pytest.fixture
def provider(networks):
    with networks.zksync.era_sepolia.use_provider("zksync") as p:
        yield p


def test_connect(provider):
    assert provider.chain_id == 300


def test_get_block(provider):
    block = provider.get_block("latest")
    assert block.number >= 0


def test_l1_batch_number(provider):
    batch = provider.get_zksync_l1_batch_number()
    assert batch is not None and batch >= 0


def test_main_contract(provider):
    addr = provider.get_zksync_main_contract()
    assert addr is not None and addr.startswith("0x")
