from medassist_agent.agent import SimpleMemory

def test_memory_log_and_load(tmp_path):
    # Notice the 4 spaces of indentation here
    p = tmp_path / "mem.json"
    mem = SimpleMemory(path=str(p))
    mem.save_profile('p1', {'name': 'Alice'})
    assert mem.load_profile('p1')['name'] == 'Alice'
    mem.log_adherence('p1', 'DrugA', '2025-11-24T00:00:00Z', 'taken')
    rows = mem.get_recent_adherence('p1', days=365)
    assert any(r['med_name'] == 'DrugA' for r in rows)