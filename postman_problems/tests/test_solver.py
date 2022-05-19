import pytest
from postman_problems.solver import cpp, rpp
from postman_problems.graph import read_edgelist
from postman_problems.tests.test_stats import (
    test_stats_on_simple_graph_required_edges_only,
    test_stats_on_star_graph_with_optional_edges
)


def test_cpp_graph_1(GRAPH_1_EDGELIST_CSV):
    edges = read_edgelist(GRAPH_1_EDGELIST_CSV, keep_optional=False)
    circuit, graph = cpp(edges, start_node='a')
    assert len(circuit) == 7

    # Re-use the test for the summary_stats function to ensure CPP solution is correct
    test_stats_on_simple_graph_required_edges_only(circuit)


def test_rpp_graph_2(GRAPH_2_EDGELIST_CSV):
    edges = read_edgelist(GRAPH_2_EDGELIST_CSV, keep_optional=True)
    circuit, graph = rpp(edges, start_node='a')
    assert len(circuit) == 6

    # Re-use the test for the summary_stats function to ensure RPP solution is correct
    test_stats_on_star_graph_with_optional_edges(circuit)


def test_rpp_graph_3(GRAPH_3_EDGELIST_CSV):
    """Testing that RPP fails on graph with 2 connected components when optional edges are removed."""
    with pytest.raises(AssertionError):
        edges = read_edgelist(GRAPH_3_EDGELIST_CSV, keep_optional=True)
        _, _ = rpp(edges, start_node='a')



