# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
    )

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
    )

    formats = formats_male + formats_female
    
    # source: http://www.bfs.admin.ch/bfs/portal/fr/index/news/publikationen.html?publicationID=6704
    first_names_male = ['Alain', 'Albert', 'Alexandre', 'André', 'Antonio', 
        'Arthur', 'Bernard', 'Bruno', 'Charles', 'Christian', 'Christophe', 
        'Claude', 'Daniel', 'David', 'Eric', 'Ethan', 'Florian', 'François',
        'Frédéric', 'Gabriel', 'Georges', 'Gilbert', 'Guillaume', 'Gérard', 
        'Henri', 'Hugo', 'Jacques', 'Jean', 'Jean-Claude', 'Jean-Pierre', 
        'Jonathan', 'José', 'Julien', 'Kevin', 'Laurent', 'Louis', 'Loïc', 
        'Luca', 'Lucas', 'Léo', 'Manuel', 'Marcel', 'Mathieu', 'Matteo', 
        'Maurice', 'Maxime', 'Michael', 'Michel', 'Nathan', 'Nicolas', 'Noah',
        'Nolan', 'Olivier', 'Pascal', 'Patrick', 'Paul', 'Philippe', 'Pierre',
        'Raymond', 'René', 'Robert', 'Roger', 'Roland', 'Romain', 'Samuel', 
        'Stéphane', 'Sébastien', 'Thierry', 'Thomas', 'Théo', 'Vincent'
    ]

    first_names_female = ['Alice', 'Alicia', 'Ana', 'Anna', 'Anne', 'Aurélie',
        'Camille', 'Caroline', 'Catherine', 'Chantal', 'Charlotte', 'Chloé', 
        'Christiane', 'Christine', 'Clara', 'Claudine', 'Corinne', 'Céline', 
        'Danielle', 'Denise', 'Eliane', 'Elisa', 'Elisabeth', 'Elodie', 
        'Emilie', 'Emma', 'Eva', 'Fabienne', 'Françoise', 'Georgette', 
        'Germaine', 'Hélène', 'Isabelle', 'Jacqueline', 'Jeanne', 'Jessica',
        'Josiane', 'Julie', 'Laetitia', 'Lara', 'Laura', 'Laurence', 'Liliane',
        'Lisa', 'Lucie', 'Léa', 'Madeleine', 'Manon', 'Marcelle', 'Marguerite',
        'Maria', 'Marianne', 'Marie', 'Mathilde', 'Monique', 'Mélanie', 
        'Nathalie', 'Nelly', 'Nicole', 'Odette', 'Patricia', 'Sandra', 
        'Sandrine', 'Sara', 'Sarah', 'Simone', 'Sophie', 'Stéphanie', 'Suzanne',
        'Sylvie', 'Thérèse', 'Valérie', 'Vanessa', 'Véronique', 'Yvette', 
        'Yvonne', 'Zoé'
    ]
    
    first_names = first_names_male + first_names_female

    # source = http://kunden.eye.ch/swissgen/rsr/index.html
    last_names = ['Aebi', 'Aeby', 'Alber', 'Babey', 'Badan', 'Badel', 'Bahon', 
        'Balmat', 'Barbey', 'Barillon', 'Barman', 'Bavaud', 'Beguin', 
        'Berberat', 'Bernasconi', 'Besançon', 'Besençon', 'Besse', 'Beuchat',
        'Beuret', 'Beurret', 'Blanc', 'Bochud', 'Boechat', 'Boichat', 'Boillat',
        'Bonvin', 'Bonvini', 'Botteron', 'Bourquard', 'Bourquin', 'Bouvier', 
        'Bovet', 'Brahier', 'Brandt', 'Broquet', 'Bugnon', 'Bujard', 'Béguelin',
        'Candaux', 'Carraud', 'Carraux', 'Carron', 'Cattin', 'Chappuis', 
        'Chapuis', 'Charpié', 'Chatriand', 'Chatriant', 'Chaudet', 'Chenaux',
        'Chevalley', 'Chevrolet', 'Chopard', 'Coigny', 'Comman', 'Comment',
        'Comte', 'Conrad', 'Corbat', 'Corboz', 'Cornut', 'Cornuz', 'Corpataux',
        'Cosandey', 'Cosendey', 'Cossy', 'Courvoisier', 'Cousin', 'Cretton', 
        'Crevoisier', 'Crivelli', 'Curdy', 'de Dardel', 'Deladoëy', 'Delèze',
        'Deshusses', 'Diesbach', 'Droz', 'Dubey', 'Duroux', 'Duvanel', 'Délèze',
        'Evéquoz', 'Fonjallaz', 'Francillon', 'Galland', 'Georges', 'Gillièron',
        'Gilliéron', 'Godet', 'Grand', 'Grojean', 'Grosjean', 'Gubéran', 
        'Humbert', 'Isella', 'Jacot-Descombes', 'Jacot-Guillarmod', 'Joly', 
        'Jomini', 'Joye', 'Julliard', 'Maire', 'Marti', 'Martin', 'Marty', 
        'Masseron', 'Matile', 'Mayor', 'Menthonnex', 'Mercier', 'Meyer', 
        'Monnard', 'Monnet', 'Monnet', 'Monney', 'Montandon', 'Morand', 
        'Morard', 'Mottet', 'Mottiez', 'Muriset', 'Musy', 'Müller', 'Niquille',
        'Nusslé', 'Nüsslin', 'Paccot', 'Pachoud', 'Paschoud', 'Pasquier', 
        'Peitrequin', 'Pellet', 'Piccand', 'Polla', 'Privet', 'Quartier', 
        'Rapin', 'Rappaz', 'Rapraz', 'Rey', 'Robadey', 'Robert', 'Romanens', 
        'Rosselat', 'Rosselet', 'Rossellat', 'Sandoz', 'Sansonnens', 'Saudan',
        'Thorens', 'Théraulaz', 'Tinguely', 'Treboux', 'Uldry', 'Vallélian',
        'Vermeil', 'Vienne', 'Vonlanthen', 'Vuille', 'Wicht'
    ] 
