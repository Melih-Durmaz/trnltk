# coding=utf-8
import os
import unittest
from hamcrest import *
from trnltk.stem.dictionaryitem import DictionaryItem, PrimaryPosition, RootAttribute, SecondaryPosition
from trnltk.stem.dictionaryloader import DictionaryLoader

class DictionaryLoaderTest(unittest.TestCase):
    def test_should_create_dictionary_item_from_line(self):
        
        item = DictionaryLoader._crate_dictionary_item_from_line(u'a [P:Interj]')
        assert_that(item, equal_to(DictionaryItem(u"a", u"a", PrimaryPosition.INTERJECTION, None, None)))
        
        item = DictionaryLoader._crate_dictionary_item_from_line(u'aba [P:Adj]')
        assert_that(item, equal_to(DictionaryItem(u"aba", u"aba", PrimaryPosition.ADJECTIVE, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'abadî')
        assert_that(item, equal_to(DictionaryItem(u"abadî", u"abadî", None, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'abat [P:Adj; A:NoVoicing]')
        assert_that(item, equal_to(DictionaryItem(u"abat", u"abat", PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'Abdal')
        assert_that(item, equal_to(DictionaryItem(u"Abdal", u"Abdal", None, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'abdest [A:NoVoicing]')
        assert_that(item, equal_to(DictionaryItem(u"abdest", u"abdest", None, None, [RootAttribute.NoVoicing])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'abes [P:Adv]')
        assert_that(item, equal_to(DictionaryItem(u"abes", u"abes", PrimaryPosition.ADVERB, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'ablak [P:Adj; A:NoVoicing]')
        assert_that(item, equal_to(DictionaryItem(u"ablak", u"ablak", PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'abuk [P:Adj, Dup;A:NoVoicing, NoSuffix]')
        assert_that(item, equal_to(DictionaryItem(u"abuk", u"abuk", PrimaryPosition.ADJECTIVE, SecondaryPosition.DUPLICATOR, [RootAttribute.NoVoicing, RootAttribute.NoSuffix])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'acemborusu [A:CompoundP3sg; R:acemboru]')
        assert_that(item, equal_to(DictionaryItem(u"acemborusu", u"acemboru", None, None, [RootAttribute.CompoundP3sg])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'acembuselik')
        assert_that(item, equal_to(DictionaryItem(u"acembuselik", u"acembuselik", None, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'aciz [A: LastVowelDrop]')
        assert_that(item, equal_to(DictionaryItem(u"aciz", u"aciz", None, None, [RootAttribute.LastVowelDrop])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'âciz [P:Adj]')
        assert_that(item, equal_to(DictionaryItem(u"âciz", u"âciz", PrimaryPosition.ADJECTIVE, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'açık [P:Adj]')
        assert_that(item, equal_to(DictionaryItem(u"açık", u"açık", PrimaryPosition.ADJECTIVE, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'ad')
        assert_that(item, equal_to(DictionaryItem(u"ad", u"ad", None, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'ad [P:Noun; A:Doubling, InverseHarmony]')
        assert_that(item, equal_to(DictionaryItem(u"ad", u"ad", PrimaryPosition.NOUN, None, [RootAttribute.Doubling, RootAttribute.InverseHarmony])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'addetmek [A:Voicing, Aorist_A]')
        assert_that(item, equal_to(DictionaryItem(u"addetmek", u"addetmek", None, None, [RootAttribute.Voicing, RootAttribute.Aorist_A])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'addolmak')
        assert_that(item, equal_to(DictionaryItem(u"addolmak", u"addolmak", None, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'ahlat [A:NoVoicing, Plural]')
        assert_that(item, equal_to(DictionaryItem(u"ahlat", u"ahlat", None, None, [RootAttribute.NoVoicing, RootAttribute.Plural])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'akşam [P:Noun, Time; S:+Rel_ki]')
        assert_that(item, equal_to(DictionaryItem(u"akşam", u"akşam", PrimaryPosition.NOUN, SecondaryPosition.TIME, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'yemek [P:Noun]')
        assert_that(item, equal_to(DictionaryItem(u"yemek", u"yemek", PrimaryPosition.NOUN, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'yemek')
        assert_that(item, equal_to(DictionaryItem(u"yemek", u"yemek", None, None, None)))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'ürkmek [A:Causative_It]')
        assert_that(item, equal_to(DictionaryItem(u"ürkmek", u"ürkmek", None, None, [RootAttribute.Causative_It])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'akşamsefası [A:CompoundP3sg; R:akşamsefa]')
        assert_that(item, equal_to(DictionaryItem(u"akşamsefası", u"akşamsefa", None, None, [RootAttribute.CompoundP3sg])))

        item = DictionaryLoader._crate_dictionary_item_from_line(u'akşamüstü [P:Noun, Time; A:CompoundP3sg; R:akşamüst]')
        assert_that(item, equal_to(DictionaryItem(u"akşamüstü", u"akşamüst", PrimaryPosition.NOUN, SecondaryPosition.TIME, [RootAttribute.CompoundP3sg])))

    def test_should_not_set_position_and_lemma_if_position_is_set_already(self):
        item_org = DictionaryItem(u'elma', u'elma', PrimaryPosition.NOUN, None, None)
        item_clone = item_org.clone()
        DictionaryLoader._set_position_and_lemma(item_clone)
        assert_that(item_org, equal_to(item_clone))

        item_org = DictionaryItem(u'mavi', u'mavi', PrimaryPosition.ADJECTIVE, None, None)
        item_clone = item_org.clone()
        DictionaryLoader._set_position_and_lemma(item_clone)
        assert_that(item_org, equal_to(item_clone))

        item_org = DictionaryItem(u'aha', u'aha', PrimaryPosition.INTERJECTION, None, None)
        item_clone = item_org.clone()
        DictionaryLoader._set_position_and_lemma(item_clone)
        assert_that(item_org, equal_to(item_clone))

        item_org = DictionaryItem(u'yemek', u'yemek', PrimaryPosition.NOUN, None, None)
        item_clone = item_org.clone()
        DictionaryLoader._set_position_and_lemma(item_clone)
        assert_that(item_org, equal_to(item_clone))

        item_org = DictionaryItem(u'tokmak', u'tokmak', PrimaryPosition.NOUN, None, None)
        item_clone = item_org.clone()
        DictionaryLoader._set_position_and_lemma(item_clone)
        assert_that(item_org, equal_to(item_clone))

    def test_should_set_position_and_lemma_for_nonverbs(self):
        item = DictionaryItem(u'elma', u'elma', None, None, None)
        DictionaryLoader._set_position_and_lemma(item)
        assert_that(item, equal_to(DictionaryItem(u'elma', u'elma', PrimaryPosition.NOUN, None, None)))

    def test_should_set_position_and_lemma_for_verbs(self):
        item = DictionaryItem(u'yemek', u'yemek', None, None, None)
        DictionaryLoader._set_position_and_lemma(item)
        assert_that(item, equal_to(DictionaryItem(u'yemek', u'ye', PrimaryPosition.VERB, None, None)))

        item = DictionaryItem(u'elemek', u'elemek', None, None, None)
        DictionaryLoader._set_position_and_lemma(item)
        assert_that(item, equal_to(DictionaryItem(u'elemek', u'ele', PrimaryPosition.VERB, None, None)))

    def test_should_infer_morphemic_attrs_for_verbs(self):
        PVD = RootAttribute.ProgressiveVowelDrop
        PI = RootAttribute.Passive_In
        AA = RootAttribute.Aorist_A
        AI = RootAttribute.Aorist_I
        VO = RootAttribute.Voicing
        NVO = RootAttribute.NoVoicing

        C_T = RootAttribute.Causative_t
        C_IR = RootAttribute.Causative_Ir
        C_IT = RootAttribute.Causative_It
        C_AR = RootAttribute.Causative_Ar
        C_DIR = RootAttribute.Causative_dIr

        item = DictionaryItem(u'gitmek', u'git', PrimaryPosition.VERB, None, [VO, C_DIR])
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'gitmek', u'git', PrimaryPosition.VERB, None, [VO, C_DIR, AA])))

        item = DictionaryItem(u'gelmek', u'gel', PrimaryPosition.VERB, None, [AI, C_DIR])
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'gelmek', u'gel', PrimaryPosition.VERB, None, [AI, C_DIR, PI, NVO])))

        item = DictionaryItem(u'atmak', u'at', PrimaryPosition.VERB, None, [NVO, C_DIR])
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'atmak', u'at', PrimaryPosition.VERB, None, [NVO, C_DIR, AA])))

        item = DictionaryItem(u'atamak', u'ata', PrimaryPosition.VERB, None, None)
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'atamak', u'ata', PrimaryPosition.VERB, None, [PVD, PI, AI, C_T, NVO])))

        item = DictionaryItem(u'dolamak', u'dola', PrimaryPosition.VERB, None, None)
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'dolamak', u'dola', PrimaryPosition.VERB, None, [PVD, PI, AI, C_T, NVO])))

        item = DictionaryItem(u'tanımak', u'tanı', PrimaryPosition.VERB, None, [AI])
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'tanımak', u'tanı', PrimaryPosition.VERB, None, [AI, PVD, PI, AI, C_T, NVO])))

        item = DictionaryItem(u'getirmek', u'getir', PrimaryPosition.VERB, None, [AI])
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'getirmek', u'getir', PrimaryPosition.VERB, None, [AI, AI, C_T, NVO])))

        item = DictionaryItem(u'ürkmek', u'ürk', PrimaryPosition.VERB, None, [C_IT])
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'ürkmek', u'ürk', PrimaryPosition.VERB, None, [C_IT, AA, NVO])))

        item = DictionaryItem(u'ağlamak', u'ağla', PrimaryPosition.VERB, None, None)
        DictionaryLoader._infer_morphemic_attributes(item)
        assert_that(item, equal_to(DictionaryItem(u'ağlamak', u'ağla', PrimaryPosition.VERB, None, [PVD, PI, AI, C_T, NVO])))

    def test_should_load_dictionary_from_str(self):
        dictionary_content = u'''
            a [P:Interj]
            aba [P:Adj]
            abadî
            abat [P:Adj; A:NoVoicing]
            Abdal
            abdest [A:NoVoicing]
            abes [P:Adj]
            abes [P:Adv]
            ablak [P:Adj; A:NoVoicing]
            abuk [P:Adj, Dup;A:NoVoicing, NoSuffix]
            acemborusu [A:CompoundP3sg; R:acemboru]
            acembuselik
            aciz [A:LastVowelDrop]
            âciz [P:Adj]
            açık [P:Adj]
            ad
            ad [P:Noun; A:Doubling, InverseHarmony]
            addetmek [A:Voicing, Aorist_A]
            addolmak [A:Causative_dIr]
            ahlat [A:NoVoicing, Plural]
            akşam [P:Noun, Time; S:+Rel_ki]
            atamak [A:Causative_It]
            yemek [P:Noun]
            yemek [A:Causative_dIr]
            ürkmek [A:Causative_It]
        '''
        dictionary_lines = dictionary_content.split('\n')
        dictionary_lines = [l.strip() for l in dictionary_lines]
        dictionary_lines = filter(lambda line: line, dictionary_lines)

        dictionary_items = DictionaryLoader.load_from_lines(dictionary_lines)

        assert_that(dictionary_items, has_length(len(dictionary_lines)), str(len(dictionary_items)-len(dictionary_lines)))

        assert_that(dictionary_items, has_item(DictionaryItem(u'a', u'a', PrimaryPosition.INTERJECTION, None, None)))
        assert_that(dictionary_items, has_item(DictionaryItem(u'aba', u'aba', PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'abadî', u'abadî', PrimaryPosition.NOUN, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'abat', u'abat', PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'Abdal', u'Abdal', PrimaryPosition.NOUN, SecondaryPosition.PROPER_NOUN, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'abdest', u'abdest', PrimaryPosition.NOUN, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'abes', u'abes', PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'abes', u'abes', PrimaryPosition.ADVERB, None, None)))
        assert_that(dictionary_items, has_item(DictionaryItem(u'ablak', u'ablak', PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'abuk', u'abuk', PrimaryPosition.ADJECTIVE, SecondaryPosition.DUPLICATOR, [RootAttribute.NoSuffix, RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'acemborusu', u'acemboru', PrimaryPosition.NOUN, None, [RootAttribute.CompoundP3sg, RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'acembuselik', u'acembuselik', PrimaryPosition.NOUN, None, [RootAttribute.Voicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'aciz', u'aciz', PrimaryPosition.NOUN, None, [RootAttribute.LastVowelDrop, RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'âciz', u'âciz', PrimaryPosition.ADJECTIVE, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'açık', u'açık', PrimaryPosition.ADJECTIVE, None, [RootAttribute.Voicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'ad', u'ad', PrimaryPosition.NOUN, None, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'ad', u'ad', PrimaryPosition.NOUN, None, [RootAttribute.Doubling, RootAttribute.InverseHarmony, RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'addetmek', u'addet', PrimaryPosition.VERB, None, [RootAttribute.Aorist_A, RootAttribute.Causative_dIr, RootAttribute.Voicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'addolmak', u'addol', PrimaryPosition.VERB, None, [RootAttribute.Aorist_I, RootAttribute.Causative_dIr, RootAttribute.NoVoicing, RootAttribute.Passive_In])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'ahlat', u'ahlat', PrimaryPosition.NOUN, None, [RootAttribute.NoVoicing, RootAttribute.Plural])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'akşam', u'akşam', PrimaryPosition.NOUN, SecondaryPosition.TIME, [RootAttribute.NoVoicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'atamak', u'ata', PrimaryPosition.VERB, None, [RootAttribute.Aorist_I, RootAttribute.Causative_It, RootAttribute.NoVoicing, RootAttribute.Passive_In, RootAttribute.ProgressiveVowelDrop])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'yemek', u'yemek', PrimaryPosition.NOUN, None, [RootAttribute.Voicing])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'yemek', u'ye', PrimaryPosition.VERB, None, [RootAttribute.Aorist_A, RootAttribute.Causative_dIr, RootAttribute.NoVoicing, RootAttribute.Passive_In, RootAttribute.ProgressiveVowelDrop])))
        assert_that(dictionary_items, has_item(DictionaryItem(u'ürkmek', u'ürk', PrimaryPosition.VERB, None, [RootAttribute.Aorist_A, RootAttribute.Causative_It, RootAttribute.NoVoicing])))


    def test_should_validate_master_dict(self):
        path = os.path.join(os.path.dirname(__file__), '../../resources/master_dictionary.txt')

        items = DictionaryLoader.load_from_file(path)
        assert_that(len(items)>0, equal_to(True))
        for item in items:
            assert_that(item.lemma, not_none(), str(item))
            assert_that(item.root, not_none(), str(item))
            assert_that(item.primary_position, not_none(), str(item))
            assert_that(PrimaryPosition.ALL, has_item(item.primary_position), str(item))

            if item.secondary_position:
                assert_that(SecondaryPosition.ALL, has_item(item.secondary_position), str(item))

            if item.attributes:
                for attr in item.attributes:
                    assert_that(RootAttribute.ALL, has_item(attr), str(item))

if __name__ == '__main__':
    unittest.main()