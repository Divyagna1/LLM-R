import pyreason as pr

# Modify the paths based on where you've stored the files we made above
graph_path = 'graph.graphml'
labels_path = 'labels.yaml'
facts_path = 'facts.yaml'
rules_path = 'rules.yaml'

# Modify pyreason settings to make verbose and to save the rule trace to a file
pr.settings.verbose = True    # Print info to screen
pr.settings.atom_trace = True # This allows us to view all the atoms that have made a certain rule fire

# Load all the files into pyreason
pr.load_graph(graph_path)
pr.load_labels(labels_path)
pr.load_facts(facts_path)
pr.load_rules(rules_path)

# Run the program for two timesteps to see the diffusion take place
interpretation = pr.reason(timesteps=2)

# Display the changes in the interpretation for each timestep
dataframes = pr.filter_and_sort_nodes(interpretation, ['popular'])
for t, df in enumerate(dataframes):
    print(f'TIMESTEP - {t}')
    print(df)
    print()

# Save all changes made to the interpretations a file. This is the explainability component
pr.save_rule_trace(interpretation)