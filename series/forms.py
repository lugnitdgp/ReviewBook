from django import forms

from series.models import EpisodeReview, Series

class GiveReviewForm(forms.ModelForm):

    class Meta:
        model=EpisodeReview
        fields = ['title', 'body', 'rating']

class UpdateReviewForm(forms.ModelForm):

    class Meta:
        model = EpisodeReview
        fields = ['title', 'body', 'rating']

    def save(self, commit=True):
        review = self.instance
        review.title = self.cleaned_data['title']
        review.body = self.cleaned_data['body']
        review.rating = self.cleaned_data['rating']

        if commit:
            review.save()

        return review

class AddSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['name', 'release_date', 'description', 'star', 'genre', 'director', 'running_time', 'total_episode', 'total_season', 'nor', 'publication', 'image']

